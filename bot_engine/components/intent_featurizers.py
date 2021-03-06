from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import logging
import typing
import os
import io
import re

import pandas as pd
import numpy as np
from future.utils import PY3
from typing import Any, Dict, List, Optional, Text

from rasa_nlu import utils
from rasa_nlu.featurizers import Featurizer
from rasa_nlu.training_data import Message
from rasa_nlu.training_data import TrainingData
from rasa_nlu.components import Component
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Metadata

#import bundesbot.components.tfidf as tfidf
from sklearn.feature_extraction.text import TfidfVectorizer, VectorizerMixin

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    import sklearn


class TfIdfFeaturizer(Featurizer):
    """Bag of words/ngrams tfidf featurizer

    Creates bag-of-words representation of intent features
    using sklearn's `TfidfVectorizer`.
    All tokens which consist only of digits (e.g. 123 and 99
    but not ab12d) will be represented by a single feature."""

    name = "intent_featurizer_tfidf_vectors"

    provides = ["text_features"]

    requires = []

    defaults = {
        # the parameters are taken from
        # sklearn's Tfidf

        # regular expression for tokens
        "token_pattern": r'(?u)\b\w\w+\b',

        # remove accents during the preprocessing step
        "strip_accents": None,  # {'ascii', 'unicode', None}

        # list of stop words
        "stop_words": None,  # string {'english'}, list, or None (default)

        # min document frequency of a word to add to vocabulary
        # float - the parameter represents a proportion of documents
        # integer - absolute counts
        "min_df": 1,  # float in range [0.0, 1.0] or int

        # max document frequency of a word to add to vocabulary
        # float - the parameter represents a proportion of documents
        # integer - absolute counts
        "max_df": 1.0,  # float in range [0.0, 1.0] or int

        # char or word grams
        "analyzer":'char',

        # set range of ngrams to be extracted
        "min_ngram": 2,
        "max_ngram": 5,

        # limit vocabulary size
        "max_features": None
    }

    def __init__(self, component_config=None):
        """Construct a new count vectorizer using the sklearn framework."""

        super(TfIdfFeaturizer, self).__init__(component_config)

        # regular expression for tokens
        self.token_pattern = self.component_config['token_pattern']

        # remove accents during the preprocessing step
        self.strip_accents = self.component_config['strip_accents']

        # list of stop words
        self.stop_words = self.component_config['stop_words']

        # min number of word occurancies in the document to add to vocabulary
        self.min_df = self.component_config['min_df']

        # max number (fraction if float) of word occurancies
        # in the document to add to vocabulary
        self.max_df = self.component_config['max_df']
        # analyzer word or char
        self.analyzer = self.component_config['analyzer']
        # set ngram range
        self.min_ngram = self.component_config['min_ngram']
        self.max_ngram = self.component_config['max_ngram']

        # limit vocabulary size
        self.max_features = self.component_config['max_features']

        # declare class instance for CountVect
        self.vect = None

        # preprocessor
        self.preprocessor = lambda s: re.sub(r'\b[0-9]+\b', 'NUMBER', s.lower())

    @classmethod
    def required_packages(cls):
        # type: () -> List[Text]
        return ["sklearn"]

    def train(self, training_data, cfg=None, **kwargs):
        # type: (TrainingData, RasaNLUModelConfig, **Any) -> None
        """Take parameters from config and
            construct a new count vectorizer using the sklearn framework."""
        from sklearn.feature_extraction.text import TfidfVectorizer

        # use even single character word as a token
        self.vect = TfidfVectorizer(token_pattern=self.token_pattern,
                                    strip_accents=self.strip_accents,
                                    stop_words=self.stop_words,
                                    analyzer=self.analyzer,
                                    ngram_range=(self.min_ngram,
                                                 self.max_ngram),
                                    max_df=self.max_df,
                                    min_df=self.min_df,
                                    max_features=self.max_features,
                                    preprocessor=self.preprocessor)

        lem_exs = [self._lemmatize(example)
                   for example in training_data.intent_examples]

        try:
            X = self.vect.fit_transform(lem_exs).toarray()
        except ValueError:
            self.vect = None
            return

        for i, example in enumerate(training_data.intent_examples):
            # create bag for each example
            example.set("text_features", X[i])

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None
        if self.vect is None:
            logger.error("There is no trained CountVectorizer: "
                         "component is either not trained or "
                         "didn't receive enough training data")
        else:
            bag = self.vect.transform([self._lemmatize(message)]).toarray()
            message.set("text_features", bag)

    @staticmethod
    def _lemmatize(message,lemmatize=False):
        if message.get("spacy_doc"):
            if lemmatize:
                return ' '.join([t.lemma_ for t in message.get("spacy_doc")])
            else:
                return ' '.join([t.text for t in message.get("spacy_doc")])
        else:
            return message.text

    @classmethod
    def load(cls,
             model_dir=None,  # type: Text
             model_metadata=None,  # type: Metadata
             cached_component=None,  # type: Optional[Component]
             **kwargs  # type: **Any
             ):
        # type: (...) -> TfIdfFeaturizer

        meta = model_metadata.for_component(cls.name)
        pklfile = TfIdfFeaturizer.name+".pkl"
        if model_dir:
            featurizer_file= os.path.join(model_dir, pklfile)
            return utils.pycloud_unpickle(featurizer_file)
        else:
            logger.warning("Failed to load featurizer. Maybe path {} "
                           "doesn't exist".format(os.path.abspath(model_dir)))
            return TfIdfFeaturizer(meta)

    def persist(self, model_dir):
        # type: (Text) -> Dict[Text, Any]
        """Persist this model into the passed directory.
        Returns the metadata necessary to load the model again."""

        featurizer_file = os.path.join(model_dir, self.name + ".pkl")
        utils.pycloud_pickle(featurizer_file, self)
        return {"featurizer_file": self.name + ".pkl"}


class TfIdfCharWordFeaturizer(Featurizer):
    """Bag of words/ngrams tfidf featurizer

    Creates bag-of-words representation of intent features
    using sklearn's `TfidfVectorizer`.
    All tokens which consist only of digits (e.g. 123 and 99
    but not ab12d) will be represented by a single feature."""

    name = "intent_featurizer_char_word_gram"

    provides = ["text_features"]

    requires = []

    defaults = {
        # the parameters are taken from
        # sklearn's Tfidf

        # regular expression for tokens
        "token_pattern": r'(?u)\b\w\w+\b',

        # remove accents during the preprocessing step
        "strip_accents": None,  # {'ascii', 'unicode', None}

        # list of stop words
        "stop_words": None,  # string {'english'}, list, or None (default)

        # min document frequency of a word to add to vocabulary
        # float - the parameter represents a proportion of documents
        # integer - absolute counts
        "min_df": 1,  # float in range [0.0, 1.0] or int

        # max document frequency of a word to add to vocabulary
        # float - the parameter represents a proportion of documents
        # integer - absolute counts
        "max_df": 1.0,  # float in range [0.0, 1.0] or int

        # char or word grams
        "analyzer":'char',

        # set range of ngrams to be extracted
        "min_ngram": 3,
        "max_ngram": 5,

        # limit vocabulary size
        "max_features": None
    }

    def __init__(self, component_config=None):
        """Construct a new count vectorizer using the sklearn framework."""

        super(TfIdfCharWordFeaturizer, self).__init__(component_config)

        # regular expression for tokens
        self.token_pattern = self.component_config['token_pattern']

        # remove accents during the preprocessing step
        self.strip_accents = self.component_config['strip_accents']

        # list of stop words
        self.stop_words = self.component_config['stop_words']

        # min number of word occurancies in the document to add to vocabulary
        self.min_df = self.component_config['min_df']

        # max number (fraction if float) of word occurancies
        # in the document to add to vocabulary
        self.max_df = self.component_config['max_df']
        # analyzer word or char
        self.analyzer = self.component_config['analyzer']
        # set ngram range
        self.min_ngram = self.component_config['min_ngram']
        self.max_ngram = self.component_config['max_ngram']

        # limit vocabulary size
        self.max_features = self.component_config['max_features']

        # declare class instance for CountVect
        self.vect = None

        # preprocessor
        self.preprocessor = lambda s: re.sub(r'\b[0-9]+\b', 'NUMBER', s.lower())

    @classmethod
    def required_packages(cls):
        # type: () -> List[Text]
        return ["sklearn"]

    def train(self, training_data, cfg=None, **kwargs):
        # type: (TrainingData, RasaNLUModelConfig, **Any) -> None
        """Take parameters from config and
            construct a new count vectorizer using the sklearn framework."""
        self.vect = CategoryBasedTfIdf()
        lem_exs = [self._lemmatize(example)
                   for example in training_data.intent_examples]
        intent_labels = [message.data['intent'] for message in training_data.intent_examples]
        try:
            self.vect.fit(lem_exs,intent_labels)
            X = self.vect.transform(lem_exs).toarray()
        except ValueError:
            self.vect = None
            return

        for i, example in enumerate(training_data.intent_examples):
            # create bag for each example
            example.set("text_features", X[i])

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None
        if self.vect is None:
            logger.error("There is no trained CountVectorizer: "
                         "component is either not trained or "
                         "didn't receive enough training data")
        else:
            bag = self.vect.transform([self._lemmatize(message)]).toarray()
            message.set("text_features", bag)

    @staticmethod
    def _lemmatize(message,lemmatize=False):
        if message.get("spacy_doc"):
            if lemmatize:
                return ' '.join([t.lemma_ for t in message.get("spacy_doc")])
            else:
                return ' '.join([t.text for t in message.get("spacy_doc")])
        else:
            return message.text

    @classmethod
    def load(cls,
             model_dir=None,  # type: Text
             model_metadata=None,  # type: Metadata
             cached_component=None,  # type: Optional[Component]
             **kwargs  # type: **Any
             ):
        # type: (...) -> TfIdfCharWordFeaturizer

        meta = model_metadata.for_component(cls.name)
        pklfile = TfIdfCharWordFeaturizer.name+".pkl"
        if model_dir:
            featurizer_file= os.path.join(model_dir, pklfile)
            return utils.pycloud_unpickle(featurizer_file)
        else:
            logger.warning("Failed to load featurizer. Maybe path {} "
                           "doesn't exist".format(os.path.abspath(model_dir)))
            return TfIdfCharWordFeaturizer(meta)

    def persist(self, model_dir):
        # type: (Text) -> Dict[Text, Any]
        """Persist this model into the passed directory.
        Returns the metadata necessary to load the model again."""

        featurizer_file = os.path.join(model_dir, self.name + ".pkl")
        utils.pycloud_pickle(featurizer_file, self)
        return {"featurizer_file": self.name + ".pkl"}

class CategoryBasedTfIdf:
    # Category based tfidf
    # supervised classification tasks
    # First group all training docs according to label
    # and for each category, create one big doc.
    # then fit the tfidf vectorizer on those category-docs. It learns vocabulary and
    # tfidf weights based on these category docs.

    def __init__(self,options=None,target_names =None,top=None):
        self.target_names = target_names
        self.tfidf = TfidfVectorizer()
        analyzer = CharWordGramAnalyzer(token_pattern=self.tfidf.token_pattern)
        self.tfidf.analyzer=analyzer

    def fit(self,x,y):
        # group according to label
        dict = {'label': y, 'docs': x}
        df = pd.DataFrame().from_dict(dict)
        grouped = df.groupby(by=df['label']).count()
        category_docs = []
        for group in grouped.iterrows():
            # for each label group, get all docs
            grouped_docs = df[df['label'] == group[0]]['docs']
            # combine all docs in class
            # into one big doc.
            bigdoc = grouped_docs.str.cat(sep=' ')
            category_docs.append(bigdoc)

        print("Fitting tfidf vectorizer")
        self.tfidf.fit(category_docs)
        words = np.array(self.tfidf.get_feature_names())
        print("After fitting: ORIG vocab len {}".format(len(words)))

    def best_in_class(self,tfidf: TfidfVectorizer, docs, top=20):
        # get top best featurs in tfidf vectorizer
        if isinstance(docs, str):
            docs = [docs]
        best_word_indices = []
        for doc in docs:
            idfvect = tfidf.transform([doc])[0, :].toarray()[0]
            # sort descending
            sort_arg_desc = np.argsort(idfvect)[::-1]
            # remove zeros
            sort_arg_desc = sort_arg_desc[idfvect[sort_arg_desc] > 0.0]
            # take top
            if len(sort_arg_desc) > top:
                sort_arg_desc = sort_arg_desc[:top]
            best_word_indices.extend(sort_arg_desc)
        bwi = np.unique(best_word_indices)
        return bwi


    def transform(self,x):
        if self.tfidf is None:
            raise ValueError()
        return self.tfidf.transform(x)

class CharWordGramAnalyzer():
    def __init__(self,token_pattern,chargramrange=(3,5),wordgramrange=(1,2)):
        self.chargramrange = chargramrange
        self.wordgramrange = wordgramrange
        self.base_analyzer = VectorizerMixin()
        self.token_pattern = token_pattern
    def __call__(self, *args, **kwargs):
        return self.char_and_wordgram_features_from_docs(args[0])
    def char_and_wordgram_features_from_docs(self,doc):
        import re
        tokens = re.findall(self.token_pattern, doc)
        self.base_analyzer.ngram_range = self.chargramrange
        char_features = self.base_analyzer._char_ngrams(" ".join(tokens))
        self.base_analyzer.ngram_range = self.wordgramrange
        word_features = self.base_analyzer._word_ngrams(tokens)
        word_features.extend(char_features)
        return word_features

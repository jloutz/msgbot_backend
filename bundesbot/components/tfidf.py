from sklearn.feature_extraction.text import VectorizerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


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

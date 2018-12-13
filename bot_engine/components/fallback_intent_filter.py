from rasa_nlu.components import Component


class FallbackIntentFilter(Component):
    """ der fallback intent Filter ermöglicht es uns, alle Nutzer-Eingaben, die nicht einem Intent eindeutig
    eingeordnet werden können, in einen 'fallback intent' unterzubringen.
    Dieser fallback intent kann dann in dialog training (stories.md) verwendet werden,
    um Kontext-abhängige error-handling zu ermöglichen
    """
    def __init__(self,component_config=None,threshold=0.35, fallback_intent="fallback"):
        ## threshold -- wenn intent Erkennung unter threshold, setzte fallback intent als erkannter Intent.
        ## TODO threshold auf sinnvolle Wert setzten beim error-handling (0.1 <> 0.5)
        ## mit sehr wenig intents, soll dieser wert relativ hoch gesetzt sein
        ## fallback_intent -- name von intent. Dieser Name wird in training (stories.md) verwendet
        super().__init__(component_config)
        self.fb_threshold=threshold
        self.fallback_intent = fallback_intent

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None
        if message.data['intent']['confidence'] < self.fb_threshold:
            fb_intent = {'name':self.fallback_intent,'confidence':self.fb_threshold}
            message.data['intent'] = fb_intent
            message.data['intent_ranking'].insert(0,fb_intent)

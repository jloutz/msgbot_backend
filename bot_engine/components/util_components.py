from rasa_nlu.components import Component

class ProcessingReporter(Component):

    def train(self, training_data, cfg, **kwargs):
        pass

    def process(self, message, **kwargs):
        print(message.data["text_features"].shape)
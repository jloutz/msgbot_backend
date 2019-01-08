import subprocess
from rasa_core_sdk import Action, Tracker
import webbrowser

from rasa_core_sdk.forms import FormAction


class NameForm(FormAction):
    def name(self):
        return "name_form"

    @staticmethod
    def required_slots(tracker: Tracker):
        return ["name","age"]

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_submit',tracker)
        return []
class ActionShowRasa(Action):
    ## demo action for welcome bot
    def name(self):
        return "action_open_rasa"

    def run(self,dispatcher,tracker,domain):
        webbrowser.open('http://rasa.com/', new=2)

class ActionShowRasaDoc(Action):
    ## demo action for welcome bot
    def name(self):
        return "action_open_doc"

    def run(self,dispatcher,tracker,domain):
        webbrowser.open('http://www.rasa.com/docs/getting-started/overview/', new=2)

class ActionShowGoogleDoc(Action):
    ## demo action for welcome bot
    def name(self):
        return "action_open_googledoc"

    def run(self,dispatcher,tracker,domain):
        webbrowser.open('https://designguidelines.withgoogle.com/conversation/', new=2)
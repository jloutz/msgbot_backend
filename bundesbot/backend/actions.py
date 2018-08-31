import subprocess
from rasa_core_sdk import Action

class ActionShowCheatsheet(Action):
    ## demo action for welcome bot
    def name(self):
        return "action_show_cheatsheet"

    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_template("utter_show_cheatsheet",tracker=tracker)
        subprocess.Popen(["C:\\Projects\\bundesbot\\docs\\StadtBotShootOut.pdf"], shell=True)

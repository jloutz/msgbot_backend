import subprocess
from rasa_core_sdk import Action
import webbrowser

feldSport = ["Badminton", "Fussball", "Tennis"]
feldKultur = ["Museum","Musik","Kunst"]
feldFlüchtlinge = ["Deutschkurs","Behausung","Suppenküche"]

class ActionFluechtlingDetails(Action):
    def name(self):
        return "action_fluechtling_details"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Ich kann dir einen anderen Bereich zeigen oder dir Näheres zu den folgenden Feldern im Bereich Flüchtlingshilfe erzählen: ")
        for feldList in feldFlüchtlinge:
            dispatcher.utter_message(feldList)
        return []

class ActionKulturDetails(Action):
    def name(self):
        return "action_kultur_details"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Ich kann dir einen anderen Bereich zeigen oder dir Näheres zu den folgenden Feldern im Bereich Kultur erzählen: ")
        for feldList in feldKultur:
            dispatcher.utter_message(feldList)
        return []
class ActionSportDetails(Action):
    def name(self):
        return "action_sport_details"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Ich kann dir einen anderen Bereich zeigen oder dir Näheres zu den folgenden Feldern im Bereich Sport erzählen: ")
        for feldList in feldSport:
            dispatcher.utter_message(feldList)
        return []

class ActionFeldDetails(Action):
    def name(self):
        return "action_feld_details"

    def run(self, dispatcher, tracker, domain):
        bereich = tracker.get_slot("bereich_interesse")
        listentry = tracker.get_slot("liste_eintrag")
        listindex = 0
        if listentry == "letztes":
            listindex = -1
        else:
            listindex = int(listentry) - 1
        if bereich == "sport":
            if not (listindex >= len(feldSport)):
                feld = feldSport[listindex]
                if feld=="Badminton":
                    dispatcher.utter_template("utter_badminton_details",tracker)
                elif feld=="Fussball":
                    dispatcher.utter_template("utter_fussball_details",tracker)
                elif feld=="Tennis":
                    dispatcher.utter_template("utter_tennis_details",tracker)
                else:
                    print("stuff matched weird")
            else:
                print("Falscher Wert.")
        elif bereich == "kultur":
            if not(listindex>=len(feldKultur)):
                feld=feldKultur[listindex]
                if feld=="Museum":
                    dispatcher.utter_template("utter_museum_details",tracker)
                elif feld=="Musik":
                    dispatcher.utter_template("utter_musik_details",tracker)
                elif feld=="Kunst":
                    dispatcher.utter_template("utter_kunst_details",tracker)
                else:
                    print("stuff matched weird")

            else:
                print("Falscher Wert")

        elif bereich == "flüchtlinge":
            if not(listindex>=len(feldKultur)):
                feld=feldKultur[listindex]
                feldFlüchtlinge = ["Deutschkurs", "Behausung", "Suppenküche"]
                if feld=="Deutschkurs":
                    pass
                elif feld=="Behausung":
                    pass
                elif feld=="Suppenküche":
                    pass
                else:
                    print("stuff matched weird")
            else:
                print("Falscher Wert")

        else:
            print("bereich_interesse ist nicht wie erwartet gesetzt. Wert ist: " + bereich)


class ActionBegruessung(Action):
    def name(self):
        return "action_greeting"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_begruessung", tracker)
        dispatcher.utter_template("utter_faehigkeiten", tracker)
        dispatcher.utter_template("utter_ask_interesse", tracker)
        return []


class ActionShowRasa(Action):
    ## demo action for welcome bot
    def name(self):
        return "action_open_rasa"

    def run(self, dispatcher, tracker, domain):
        webbrowser.open('http://rasa.com/', new=2)


class ActionShowRasaDoc(Action):
    ## demo action for welcome bot
    def name(self):
        return "action_open_doc"

    def run(self, dispatcher, tracker, domain):
        webbrowser.open('http://www.rasa.com/docs/getting-started/overview/', new=2)


class ActionShowGoogleDoc(Action):
    ## demo action for welcome bot
    def name(self):
        return "action_open_googledoc"

    def run(self, dispatcher, tracker, domain):
        webbrowser.open('https://designguidelines.withgoogle.com/conversation/', new=2)

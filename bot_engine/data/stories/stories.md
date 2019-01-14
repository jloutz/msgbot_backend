## happy path: Does not know bereich
* start 
    -action_greeting
* information_interesse
    - utter_bereich_klarifikation
* auswahl_liste_bereich
    - utter_list_bereich
* information_interesse{"bereich_interesse" : "sport"}
    -slot{"bereich_interesse": "sport"}
    -action_sport_details
* auswahl_liste{"liste_eintrag" : "4"}
    -slot{"liste_eintrag" : "4"}
    - action_feld_details
    
## happy path: Does not know bereich, wants examples
* start 
    -action_greeting
* information_interesse
    - utter_bereich_klarifikation
* beispiele_konkret
    - utter_beispiele1
* weiter 
    -utter_beispiele2
* weiter
    - utter_beispiele3
    
## happy path: back and forth
    - utter_beispiele2
* zurück 
    -utter_beispiele1
* zurück
    -utter_beispiele3
* zurück 
    - utter_beispiele2
## happy path: bereich sport
* start 
    -action_greeting
* information_interesse{"bereich_interesse" : "sport"}
    - slot{"bereich_interesse": "sport"}
    - action_sport_details
* auswahl_liste{"liste_eintrag" :"1"}
    -slot{"liste_eintrag" : "1"}
    - action_feld_details

## happy path: bereich kultur
* start 
    -action_greeting
* information_interesse{"bereich_interesse" : "kultur"}
    - slot{"bereich_interesse": "kultur"}
    - action_kultur_details
* auswahl_liste{"liste_eintrag" :"2"}
    -slot{"liste_eintrag" : "2"}
    - action_feld_details
    
## happy path: bereich fluechtlinge
* start 
    -action_greeting
* information_interesse{"bereich_interesse" : "flüchtlinge"}
    - slot{"bereich_interesse": "flüchtlinge"}
    - action_fluechtling_details
* auswahl_liste{"liste_eintrag" :"3"}
    -slot{"liste_eintrag" : "3"}
    - action_feld_details
    
## unhappy path
* start 
    -action_greeting
* fallback
    - utter_bereich_klarifikation
    
##unhappy path
*fallback
    - utter_bereich_klarifikation
*fallback
    -utter_bereich_klarifikation
*fallback
    -utter_ende_konversation
    -action_restart

## Generated Story -316864321894813267
* start
    - action_greeting
* information_interesse
    - utter_bereich_klarifikation
* auswahl_liste_bereich
    - utter_list_bereich
* information_interesse{"bereich_interesse": "sport"}
    - slot{"bereich_interesse": "sport"}
    - action_sport_details
* auswahl_liste{"liste_eintrag": "1"}
    - slot{"liste_eintrag": "1"}
    - action_feld_details

## Generated Story 2799651232811535548
* start
    - action_greeting
* information_interesse{"bereich_interesse": "sport"}
    - slot{"bereich_interesse": "sport"}
    - action_sport_details
* auswahl_liste{"liste_eintrag": "2"}
    - slot{"liste_eintrag": "2"}
    - action_feld_details

## Generated Story 8659995725679220699
* start
    - action_greeting
* information_interesse{"bereich_interesse": "kultur"}
    - slot{"bereich_interesse": "kultur"}
    - action_kultur_details
* auswahl_liste{"liste_eintrag": "letztes"}
    - slot{"liste_eintrag": "letztes"}
    - action_feld_details


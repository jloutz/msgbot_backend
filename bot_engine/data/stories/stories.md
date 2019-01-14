## happy path: Does not know
* start 
    -action_greeting
* information_interesse
    - utter_bereich_klarifikation
* auswahl_liste_bereich
    - utter_list_bereich
* information_interesse{"bereich_interesse" : "sport"}
    -slot{"bereich_interesse": "sport"}
    -action_sport_details
* auswahl_liste{"liste_eintrag" : "1"}
    -slot{"liste_eintrag" : "1"}
    - action_feld_details
    
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


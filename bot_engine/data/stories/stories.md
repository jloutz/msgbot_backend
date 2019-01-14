## happy path: Does not know
* start 
    -action_greeting
* information_interesse
    - utter_bereich_klarifikation
* auswahl_liste_bereich
    - utter_list_bereich
* information_interesse{"bereich_interesse" : "sport"}
    -slot{"bereich_interesse": "sport"}
    -utter_sport_details
* auswahl_liste
    - utter_feld_details
    
## happy path: bereich sport
* start 
    -action_greeting
* information_interesse{"bereich_interesse" : "sport"}
    - slot{"bereich_interesse": "sport"}
    - utter_sport_details
* auswahl_liste
    - utter_feld_details
## Generated Story -2845097536574265860
* start
    -action_greeting
* information_interesse
    - utter_bereich_klarifikation
* auswahl_liste
    - utter_list_bereich
* information_interesse{"bereich_interesse": "sport"}
    - slot{"bereich_interesse": "sport"}
    - utter_sport_details
* auswahl_liste
    - utter_feld_details

## Generated Story 4109247210663124599
* start
    -action_greeting
* information_interesse{"bereich_interesse": "sport"}
    - slot{"bereich_interesse": "sport"}
    - utter_sport_details
* auswahl_liste
    - utter_feld_details


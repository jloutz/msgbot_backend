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

## building block: wants badminton
* interesse_badminton
    -utter_badminton_details
    
## building block: wants fussball
* interesse_fussball
    -utter_fussball_details
    
    
## building block: wants tennis
* interesse_tennis
    -utter_tennis_details
    
## building block: wants museum
* interesse_museum
    -utter_museum_details
    
## building block: wants musik
* interesse_musik
    -utter_musik_details
    
## building block: wants kunst
* interesse_kunst
    -utter_kunst_details
    
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

## Generated Story 6707480065510242378
* start
    - action_greeting
* information_interesse
    - utter_bereich_klarifikation
* beispiele_konkret
    - utter_beispiele1
* weiter
    - utter_beispiele2
* weiter
    - utter_beispiele3

## Generated Story 5481385524056445540
* start
    - action_greeting
* information_interesse
    - utter_bereich_klarifikation
* beispiele_konkret
    - utter_beispiele1
* zurück
    - utter_beispiele3

## Generated Story 4525603202407279251
* start
    - action_greeting
* information_interesse{"bereich_interesse": "fl\u00fcchtlinge"}
    - slot{"bereich_interesse": "fl\u00fcchtlinge"}
    - action_fluechtling_details
* auswahl_liste{"liste_eintrag": "1"}
    - slot{"liste_eintrag": "1"}
    - action_feld_details

## Generated Story -9037978774805181019
* start
    - action_greeting
* information_interesse
    - utter_bereich_klarifikation
* auswahl_liste_bereich{"PER": "Zeig"}
    - utter_list_bereich
* information_interesse{"bereich_interesse": "kultur"}
    - slot{"bereich_interesse": "kultur"}
    - action_kultur_details
* auswahl_liste{"liste_eintrag": "2"}
    - slot{"liste_eintrag": "2"}
    - action_feld_details

## Generated Story -6729777404838759550
* start
    - action_greeting
* information_interesse{"bereich_interesse": "fl\u00fcchtlinge"}
    - slot{"bereich_interesse": "fl\u00fcchtlinge"}
    - action_fluechtling_details
* auswahl_liste{"liste_eintrag": "2"}
    - slot{"liste_eintrag": "2"}
    - action_feld_details

## Generated Story -3600364210975583191
* start
    - action_greeting
* interesse_badminton
    - utter_badminton_details

## Generated Story 7483388882428997534
* start
    - action_greeting
* interesse_tennis
    - utter_tennis_details

## Generated Story -3073634602649486930
* start
    - action_greeting
* interesse_fussball
    - utter_fussball_details

## Generated Story -712707802653501197
* start
    - action_greeting
* interesse_fussball
    - utter_fussball_details

## Generated Story -1372487381279897231
* start
    - action_greeting
* interesse_kunst
    - utter_kunst_details

## Generated Story 6279759184057738619
* start
    - action_greeting
* interesse_musik
    - utter_musik_details

## Generated Story -3090019378127258292
* start
    - action_greeting
* interesse_museum
    - utter_museum_details


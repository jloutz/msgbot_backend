## generic eherenamt specification
* ehrenamtlich_allgemein
    - utter_greeting_explanation
* zeit_information_4plus
    - utter_question_type
* ehrenamt_fluechtlinge
    - action_specific_answer
    
## happy path
* begruessung
    - utter_greeting_explanation
    - name_form
    - form{"name": "name_form"}
    - slot{"requested_slot":"name"}

## Greeting exchange
* begruessung
    - utter_greeting_explanation

## What is Ehrenamt?
* was_ist_ehrenamt
    - utter_explanation_ehrenamt    

## Why ehrenamt
* warum_ehrenamt
    -utter_explanation_why_ehrenamt

## genereic ehrenamt specification 2
* arten_ehrenamt
    - utter_explanation_type
* ehrenamt_fluechtlinge
    - action_specific_answer
    
## Ich will fluechtlingen helfen, generic story
* ehrenamt_fluechtlinge
    - utter_question_time
* zeit_information_4plus
    - action_specific_answer
       

    
## Generated Story 714737408456433578
* begruessung
    - utter_greeting_explanation
    - name_form
    - form{"name": "name_form"}
    - slot{"requested_slot": "name"}
* form: inform{"name": "lukas"}
    - form: name_form
    - slot{"name": "lukas"}
    - slot{"requested_slot": "age"}
* form: inform{"age": "24"}
    - form: name_form
    - slot{"age": "24"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 1063031522817825891
* begruessung{"name": "john"}
    - utter_greeting_explanation
    - name_form
    - form{"name": "name_form"}
    - slot{"requested_slot": "name"}
* form: inform{"name": "John", "age": "24"}
    - form: name_form
    - slot{"age": "24"}
    - slot{"name": "John"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -170588419855504386
* begruessung
    - utter_greeting_explanation
    - name_form
    - form{"name": "name_form"}
    - slot{"requested_slot": "name"}
* form: inform{"name": "Roman"}
    - form: name_form
    - slot{"name": "Roman"}
    - slot{"requested_slot": "age"}
* form: inform{"age": "13"}
    - form: name_form
    - slot{"age": "13"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -1912393004255532548
* begruessung
    - utter_greeting_explanation
    - name_form
    - form{"name": "name_form"}
    - slot{"requested_slot": "name"}
* form: inform{"name": "lukas"}
    - form: name_form
    - slot{"name": "lukas"}
    - slot{"requested_slot": "age"}
* form: inform{"age": "999"}
    - form: name_form
    - slot{"age": "999"}
    - form{"name": null}
    - slot{"requested_slot": null}


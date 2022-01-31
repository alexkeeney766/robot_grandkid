from typing import Any, Dict, List, Optional, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

from .question import (
    make_question,
    get_required_entities,
)

class ActionSearchDocs(Action):
    def name(self) -> str:
        return "action_search_docs"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        # Get all Question in Que
        questions = tracker.get_slot("questions")
        
        # If there are no Que-ed quetsions
        if questions is None:
            # Get intent of most recent question
            intent = tracker.get_intent_of_latest_message()

            # Get related entities/slot-values
            required_entities = get_required_entities(intent)
            entities = {ent: tracker.get_slot(ent) for ent in required_entities}

            # Make Question object and return answer if all entites are present
            question = make_question(intent, entities)
        
        # If a current question exists
        else:
            question = questions.pop()
        
        # If we can answer the current question
        if len(question.missing_ents) == 0:
            dispatcher.utter_message(text=question.search_query())
            return []

        # Otherwise, ask for clarification
        else:
            dispatcher.utter_message(
                text="The following information is needed: "
                + " ".join([question.missing_ents])
            )
            questions = [question]
            return [FollowupAction(
                
            ),
            SlotSet({"quetsions": questions})]
    

                

 # Hopefully we can get this behaivor with Forms 
# class ActionEntityClarification(Action):
#     def name(self) -> str:
#         return "action_entity_clarification"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
#     ) -> List[Dict[str, Any]]:

    
# TODO: Add form validations
# class ValidateClarifySlotForm(FormValidationAction):



# TODO: Add a Question Stack, in which a user can interput a form with a question, then possibly activate
#       another form or get an immediate answer, if all required slots are already filled.
# class ActionNewQuestion(Action):
#     def name(self) -> str:
#         return "action_new_question"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
#     ) -> List[Dict[str, Any]]:

#             questions = tracker.get_slot('questions') or []
#             questions.append(question)
#             return [SlotSet({'quetsions': questions})]

# class ActionResolveQuestion(Action):

#     def name(self) -> str:
#         return "action_resolve_question"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
#     ) -> List[Dict[str, Any]]:

#         if len(questions) > 0:
#             questions.pop()

#         return []

from typing import Any, Dict, List

from rasa_sdk import Action, Tracker
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

        # Get intent of most recent question
        intent = tracker.get_intent_of_latest_message()

        # Get related entities/slot-values
        required_entities = get_required_entities(intent)
        entities = {ent: tracker.get_slot(ent) for ent in required_entities}

        # Make Question object and return answer if all entites are present
        question = make_question(intent, entities)
        if len(question.missing_ents) == 0:
            dispatcher.utter_message(text=question.search_query())
            return []

        # Otherwise, ask for clarification
        else:
            dispatcher.utter_message(
                text="The following information is needed: "
                + " ".join([question.missing_ents])
            )
            self.questions.append(question)
            questions = tracker.get_slot("questions") or []
            questions.append(question)
            return [SlotSet({"quetsions": questions})]


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

from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from .question import make_question
from .question_stack import question_stacks


class ActionNewQuestion(Action):
    """This action creates a new quetsion based on the predicted intent
    and adds it to the question_stack"""

    def name(self) -> str:
        return "action_new_question"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[str, Any]]:

        # Get intent of most recent question
        intent: str = tracker.get_intent_of_latest_message()

        # Make Question object and return answer if all entites are present
        question = make_question(intent)
        q_stack_size = question_stacks.push_question(tracker.sender_id, question)

        print(f"New question created: {question}")
        print(f"setting questions slot to : {q_stack_size}")

        return [SlotSet(key="questions", value=q_stack_size)]


class ActionResolveQuestion(Action):
    """ This action resolves an existing question, 
    removing it from the question_stack in the process"""

    def name(self) -> str:
        return "action_resolve_question"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[str, Any]]:

        # Get top quetsion from stack
        question, q_stack_len = question_stacks.pop_question(tracker.sender_id)
        print(f"stored question: {question}")

        # If we can answer the current question
        dispatcher.utter_message(text=question.resolve())
        print(f"resolved question: {question}")
        return [SlotSet(key="questions", value=q_stack_len)]

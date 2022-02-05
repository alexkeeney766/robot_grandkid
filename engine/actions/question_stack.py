from typing import Tuple
from .question import Question


class QuestionStack:
    """
    Wrapper around python dictionary for now. 
    Defines a method of storing question stacks for each
    conversation as defined by user_id in Rasa_SDK.
    """

    def __init__(self):
        self.db = {}

    def push_question(self, sender_id: int, question: Question) -> int:
        """Get the question stack if it exists, and push new question to it.
        Otherwise, make a new quetsion stack and store it in the db w/ sender_id 
        as a key.
        
        returns the length of question_stack after pushing"""
        # 'querying' database for the question stack associated with sender_id
        q_stack: list = self.db.get(sender_id, list())

        # push question to stack
        q_stack.append(question)

        # Put stack back in 'db'
        self.db[sender_id] = q_stack

        # return length
        return len(q_stack)

    def pop_question(self, sender_id: int) -> Tuple[Question, int]:
        """
        Gets and removes the next question from the sender_id's question stack.
        If this was the last question, sender_id is removed from the db.

        returns the found question, otherwise None.
        """
        # 'querying' database for the question stack associated with sender_id
        q_stack: list = self.db.pop(sender_id, [None])

        # get top question on stack
        question = q_stack.pop()
        q_stack_len = len(q_stack)

        # if q_stack is now empty, remove key (sender_id_ from db
        if q_stack_len > 0:
            self.db[sender_id] = q_stack

        return question, q_stack_len

    def set_entity_val(self, sender_id: int, slot_name:str, slot_val:str):
        # Get top quetsion from stack
        question, q_stack_len = self.pop_question(sender_id)
        print(f'Setting {slot_name} to {slot_val} in {question}')
        # Set value found
        question.set_entity(slot_name, slot_val)

        # Put question back
        self.push_question(sender_id, question)

question_stacks = QuestionStack()
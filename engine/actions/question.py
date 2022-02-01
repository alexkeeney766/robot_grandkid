from abc import ABC, abstractmethod
from tkinter.messagebox import QUESTION
from typing import Dict, List
from rasa_sdk import Action, Tracker


support_lookup = {
    "PC": "https://support.microsoft.com/search/results?query=",
    "Windows 10": "https://support.microsoft.com/search/results?query=",
    "Windows 11": "https://support.microsoft.com/search/results?query=",
    "Mac": "https://support.apple.com/kb/index?page=search&type=organic&src=support_searchbox_psp&locale=en_US&q=",
}


class EntityValueNotFoundError(Exception):
    """ raised when an entity value is not given at question init"""

    pass


class IntentNotFoundError(Exception):
    """ raised when the intent does not match a pre-made Question type """

    pass


class Question(ABC):
    required_entities = ["system"]

    def __init__(self, system: str):
        self.missing_ents = []
        self.system = system
        self.fallback_utterance = (
            "Sorry I can't do that by myself, heres a link that should help: "
        )
        self.validate_ents()

    def validate_ents(self):
        for ent in self.required_entities:
            if ent is None:
                self.missing_ents = ent

    @abstractmethod
    def search_query(self):
        pass


class FallbackQuestion(Question):
    def __init__(
        self, system: str, **entities,
    ):

        self.entities = entities
        super().__init__(system)

    def search_query(self) -> str:
        return "%20".join(
            [support_lookup[self.system]] + [val for val in self.entities.values()]
        )


class ChangeSettings(Question):
    required_entities = Question.required_entities + ["setting_name", 'desired_action']

    def __init__(
        self, system: str, setting_name: str, desired_action: str = "change",
    ):

        self.setting_name = setting_name
        self.desired_action = desired_action
        super().__init__(system)

    def search_query(self) -> str:
        return (
            support_lookup[self.system]
            + "%20"
            + "%20".join([self.desired_action, self.setting_name])
        )


class AccessingCurrentlyOpenApps(Question):

    required_entities = Question.required_entities

    def __init__(
        self, system: str,
    ):
        super().__init__(system)

    def search_query(self) -> str:
        return support_lookup[self.system] + " find currently open apps"


class OpeningPrograms(Question):
    required_entities = Question.required_entities + ["program", "desired_action"]

    def __init__(
        self, system: str, program: str, desired_action: str = "open",
    ):

        self.program = program
        self.desired_action = desired_action
        super().__init__(system)

    def search_query(self) -> str:
        return (
            support_lookup[self.system]
            + "%20"
            + "%20".join([self.desired_action, self.program])
        )


class FileManagement(Question):
    required_entities = Question.required_entities + ["file_obj", "desired_action"]

    def __init__(
        self, system: str, file_obj: str, desired_action: str = "make",
    ):

        self.file_obj = file_obj
        self.desired_action = desired_action
        super().__init__(system)

    def search_query(self) -> str:
        return (
            support_lookup[self.system]
            + "%20"
            + "%20".join([self.desired_action, self.file_obj])
        )


class Terminology(Question):
    required_entities = Question.required_entities + ["term"]

    def __init__(
        self, system: str, term: str,
    ):
        self.term = term
        super().__init__(system)

    def search_query(self) -> str:
        return support_lookup[self.system] + "%20" + self.term


question_lookup = {
    "change_settings": ChangeSettings,
    "accessing_currently_open_apps": AccessingCurrentlyOpenApps,
    "opening_programs": OpeningPrograms,
    "file_management": FileManagement,
    "terminology": Terminology,
}


def get_required_entities(intent) -> list:
    q_obj = question_lookup.get(intent, FallbackQuestion)
    try:
        return q_obj.required_entities
    except AttributeError as e:
        raise IntentNotFoundError(
            f'The intent "{intent}" does not exist in the question_lookup: \n quesion_lookup.keys = {[key for key in question_lookup.keys()]}'
        )


def make_question(intent: str, entities: dict) -> Question:
    q_obj = question_lookup.get(intent, FallbackQuestion)

    return q_obj(**entities)

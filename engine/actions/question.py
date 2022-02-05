from abc import ABC, abstractmethod
from tkinter.messagebox import QUESTION
from typing import Dict, List
from rasa_sdk import Action, Tracker


support_lookup = {
    "PC": "https://support.microsoft.com/search/results?query=",
    "Windows 10": "https://support.microsoft.com/search/results?query=",
    "Windows 11": "https://support.microsoft.com/search/results?query=",
    "Mac": "https://support.apple.com/kb/index?page=search&type=organic&src=support_searchbox_psp&locale=en_US&q=",
    "MacOS": "https://support.apple.com/kb/index?page=search&type=organic&src=support_searchbox_psp&locale=en_US&q=",
}


class EntityValueNotFoundError(Exception):
    """ raised when an entity value is not given at question init"""

    pass


class IntentNotFoundError(Exception):
    """ raised when the intent does not match a pre-made Question type """

    pass


class Question(ABC):
    required_entities = ["system"]

    def __init__(self):
        self.entities = {}

    @abstractmethod
    def resolve(self):
        pass

    def set_entity(self, ent_key: str, ent_val: str):
        if ent_key == "system":
            self.system = ent_val

        elif ent_key in self.required_entities:
            self.entities[ent_key] = ent_val


class FallbackQuestion(Question):
    def set_entity(self, ent_key: str, ent_val: str):
        if ent_key == "system":
            self.system = ent_val

        self.entities[ent_key] = ent_val

    def resolve(self) -> str:
        return (
            " ".join(
                [support_lookup[self.system]] + [val for val in self.entities.values()]
            )
            .replace("_", " ")
            .replace(" ", "%20")
        )


class ChangeSettings(Question):
    required_entities = Question.required_entities + ["setting_name", "desired_action"]

    def resolve(self) -> str:
        return (
            (
                support_lookup[self.system]
                + " "
                + " ".join(
                    [
                        self.entities.get("desired_action", "change"),
                        self.entities.get("setting_name"),
                    ]
                )
            )
            .replace("_", " ")
            .replace(" ", "%20")
        )


class AccessingCurrentlyOpenApps(Question):

    required_entities = Question.required_entities

    def resolve(self) -> str:
        return (
            (support_lookup[self.system] + " find currently open apps")
            .replace("_", " ")
            .replace(" ", "%20")
        )


class OpeningPrograms(Question):
    required_entities = Question.required_entities + ["program", "desired_action"]

    def resolve(self) -> str:
        return (
            (
                support_lookup[self.system]
                + " "
                + " ".join(
                    [
                        self.entities.get("desired_action", "open"),
                        self.entities.get("program"),
                    ]
                )
            )
            .replace("_", " ")
            .replace(" ", "%20")
        )


class FileManagement(Question):
    required_entities = Question.required_entities + ["file_obj", "desired_action"]

    def resolve(self) -> str:
        return (
            (
                support_lookup[self.system]
                + " "
                + " ".join(
                    [
                        self.entities.get("desired_action",),
                        self.entities.get("file_obj"),
                    ]
                )
            )
            .replace("_", " ")
            .replace(" ", "%20")
        )


class Terminology(Question):
    required_entities = Question.required_entities + ["term"]

    def resolve(self) -> str:
        return (
            (support_lookup[self.system] + " " + self.term)
            .replace("_", " ")
            .replace(" ", "%20")
        )


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


def make_question(intent: str) -> Question:
    q_obj = question_lookup.get(intent, FallbackQuestion)

    return q_obj()

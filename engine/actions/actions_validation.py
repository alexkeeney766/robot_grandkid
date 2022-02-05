from typing import Any, Dict, Text

from rasa_sdk import Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from .question_stack import question_stacks

class ValidateChangeSettingsForm(FormValidationAction):
    """Manages validation of slot values for change_settings_form"""

    def name(self) -> Text:
        return "validate_change_settings_form"

    def validate_system(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for system to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "system", slot_value)
        return {"system": slot_value}

    def validate_setting_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for setting_name to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "setting_name", slot_value)
        return {"setting_name": slot_value}


class ValidateCurrentlyOpenAppsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_accessing_currently_open_apps_form"

    def validate_system(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for system to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "system", slot_value)
        return {"system": slot_value}


class ValidateOpeningPrograms(FormValidationAction):
    def name(self) -> Text:
        return "validate_opening_programs_form"

    def validate_system(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for system to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "system", slot_value)
        return {"system": slot_value}

    def validate_program(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for program to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "program", slot_value)
        return {"program": slot_value}

    def validate_desired_action(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for desired_action to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "desired_action", slot_value)
        return {"desired_action": slot_value}


class ValidateFileManagement(FormValidationAction):
    def name(self) -> Text:
        return "validate_file_management_form"

    def validate_system(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for system to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "system", slot_value)
        return {"system": slot_value}

    def validate_file_obj(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for file_obj to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "file_obj", slot_value)
        return {"file_obj": slot_value}

    def validate_desired_action(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for desired_action to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "desired_action", slot_value)
        return {"desired_action": slot_value}


class ValidateTerminologyForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_terminology_form"

    def validate_system(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for system to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "system", slot_value)
        return {"system": slot_value}

    def validate_term(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Adds found slot value for term to the current Question Object"""

        question_stacks.set_entity_val(tracker.sender_id, "term", slot_value)
        return {"term": slot_value}

# For Rules later

      # - or: 
      #   - intent: accessing_currently_open_apps
      #   - intent: file_management
      #   - intent: opening_programs
      #   - intent: change_settings 
      #   - intent: terminology
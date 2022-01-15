from typing import Any, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


docs_lookup = {
    'PC': 'https://www.microsoft.com/en-us/windows/getting-started?r=1', 
    'Mac': 'https://help.apple.com/macOS/high-sierra/mac-basics/#/intro'
}

responses_lookup = {
    'PC': f"Here is Microsoft's the Getting Started Guide for your PC: {docs_lookup['PC']}",
    'Mac': f"Here is Apple's the Mac-Basics Guide for your Mac: {docs_lookup['Mac']}",
}

class ActionDocsSelector(Action):
    def name(self) -> str:
        return "action_docs_selector"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        
        dispatcher.utter_message(text=responses_lookup[tracker.get_slot('system')])

        return []

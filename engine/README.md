# Robot Grandkid

A virtual assistant for general tech support (in progress).

I'm usiing this repo to learn RASA and virtual assistants more generally.

## Initial Goal

The inital goal will be providing the correct *Getting Started* link based on the users operating system. The assistant should be able to handle chitchat, and ask the user what operating system they are using. Given this information, it should provide the correct URL, either to the Windows Getting Started page, or the MacOS Getting Started page.


## Current State:

Currently, the assistant I've trained based on these data and configurations is able to accurately classify intents, including out of scope intents and the user's OS. Given the user query: "How do I change the desktop wallpaper on my Mac?" the assistant will repond with the *Getting Started* page from Apple. Similarly, if the user asks about a PC, Microsoft's *Getting Started* page for windows is returned. If a users leaved out their system name from the query, then the assistant will recognize no entity was inlucded, and prompt the user for their OS.


## Future State/Goal

In the future, I'm hoping to generalize the assistant to provide in text answers based on the users questions, and fall back to providing search results to the users question.

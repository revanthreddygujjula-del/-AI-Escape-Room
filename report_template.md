# AI Escape Room Project Report (fill in your observations)

## Objective
The objective of this project was to develop an interactive AI-powered escape room game using Python, Streamlit, and Google's Gemini API. The game takes place in a locked library where players must explore five objects, discover clues, collect a key, and solve a four-digit passcode to escape.

## Version 1
Version 1 uses Streamlit for the chat interface and Gemini as the Game Master.

The AI interprets the player's text commands, describes the environment, provides clues, and narrates the player's progress.

Observations:

The game successfully responded to natural-language commands.

Players could explore the bookshelf, desk, painting, locked drawer, and exit door.

The player discovered the code 4729 and successfully escaped.

During development, API errors occurred, including an invalid API key, an unavailable model, and a temporary 503 service error.

Because the AI manages the game through conversation, inventory and puzzle consistency are not guaranteed.

## Version 2
Version 2 uses Python to validate player actions and maintain the game's state. Streamlit provides the interactive interface.

Python controls the puzzle rules, including whether the player has collected the brass key, unlocked the drawer, or escaped.

Observations:

The game correctly identified valid player actions.

The bookshelf revealed the first digit: 4.

The desk revealed the second digit: 7.

The painting contained a brass key.

The key unlocked the drawer, revealing the final digits: 2 and 9.

Entering 4729 successfully opened the exit door.

Incorrect actions were rejected.

## Architecture
Version 1:

Player → Streamlit Chat Interface → Gemini API → AI-generated Game Response → Player

Version 2:

Player → Streamlit Chat Interface → Python Action Validator → Game State → Validated Response → Player

The main difference is that Version 1 relies on AI-generated responses, while Version 2 uses Python to enforce game rules.

## Testing
Test Case

Expected Result

Actual Result

Look around

Display room objects

Passed

Examine bookshelf

Reveal digit 4

Passed

Examine desk

Reveal digit 7

Passed

Examine painting

Collect brass key

Passed

Unlock drawer with key

Reveal digits 2 and 9

Passed

Enter 4729

Escape successfully

Passed

Enter incorrect code 1234

Door remains locked

Passed

Unlock drawer without key

Action rejected

Passed

Restart game

Reset game progress

Passed

All nine main Version 2 functional tests passed during manual testing.

## Problems and improvements
Problem 1: API authentication

Initially, the Gemini API returned an invalid API key error.

Solution: The API configuration was corrected using the project's .env file.

Problem 2: Model availability

The originally configured Gemini model returned a 404 error because it was unavailable.

Solution: The model configuration was updated to an available model.

Problem 3: Temporary API unavailability

Version 1 encountered a 503 error due to high demand.

Solution: The request was retried successfully.

Problem 4: Game-state consistency

AI-generated game responses can be inconsistent when managing inventory and puzzle rules.

Improvement: Version 2 uses Python to validate actions and maintain authoritative game state.

Remaining limitations: Keyword-based action recognition may not understand every possible player command. More flexible command parsing and additional automated tests could improve the game.


## Conclusion
The AI Escape Room project successfully demonstrated two approaches to building an interactive escape room.

Version 1 demonstrated the use of a large language model for natural-language storytelling and player interaction.

Version 2 demonstrated how Python-controlled game logic can provide more predictable behavior, enforce puzzle rules, and prevent invalid actions.

Both versions successfully completed the escape-room challenge using the passcode 4729.

The project demonstrates the advantages of combining AI-based interaction with traditional programming for reliable interactive applications.

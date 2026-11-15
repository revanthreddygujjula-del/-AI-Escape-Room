# AI Escape Room Project Report (fill in your observations)

## Objective
Create an interactive escape-room game where an LLM narrates a library mystery, with at least five objects, clues, and an escape challenge.

## Version 1
Streamlit chat UI and Gemini Game Master. Game rules and prior messages are included in the model prompt. Limitations: model may forget inventory, invent items, or follow cheating instructions.

## Version 2
A Python action validator stores visited objects, collected key, drawer state, and escape state. Gemini can add optional narration, but cannot update the authoritative state. Invalid actions do not unlock puzzles.

## Architecture
Use the Mermaid diagrams in README.md, or export them as images.

## Testing
Fill in actual results from test_cases.md. Include screenshots of both versions, including invalid action handling and a successful escape.

## Problems and improvements
Describe actual issues observed in Version 1 and how Version 2 handled them. Note that keyword parsing is limited and narration may still be inaccurate.

## Conclusion
Summarize what you learned about LLM reliability, state validation, and GitHub project documentation.

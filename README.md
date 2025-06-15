# The Oracle's Chronicle

The Oracle's Chronicle is a fully interactive, infinite choose-your-own-adventure game powered by Python and Google's Gemini AI.

## About The Project

Unlike traditional games with pre-written paths, this project uses a live AI to act as a "Dungeon Master." It generates unique story scenes and a fresh set of choices for the player at every turn, meaning no two adventures are ever the same.

### Key Features:
- **Infinite Storylines:** The AI generates the story in real-time.
- **Dynamic Choices:** The AI also creates the choices, leading to unpredictable gameplay.
- **Dictionary-Powered State:** The game state is cleanly managed using Python dictionaries.
- **Ethical Reflection:** The program concludes with a discussion on the ethics of using generative AI.

## How to Run

1.  Make sure you have Python installed.
2.  Install the required library: `pip install google-generativeai`
3.  Download `oracle_chronicle.py`.
4.  Open the file and replace `"PASTE_YOUR_API_KEY_HERE"` with your own Google Gemini API key.
5.  Run the script from your terminal: `python oracle_chronicle.py`

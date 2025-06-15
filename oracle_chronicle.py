# ============================================================================
# THE ORACLE'S CHRONICLE
# An infinite choose-your-own-adventure powered by AI and dictionaries.
# ============================================================================

import google.generativeai as genai
import time
import os

# --- 1. CONFIGURATION ---
GEMINI_API_KEY = "PASTE_YOUR_API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. THE AI STORYTELLING ENGINE ---

def get_ai_turn(story_history):
    """
    Sends the story history to the AI and gets the next chapter.
    This is the core of the game. It asks the AI for a scene and choices.
    """
    # This prompt engineering is crucial. We are asking for a specific format.
    prompt = f"""
    You are 'The Oracle', a mystical storyteller in a fantasy text-adventure game.
    Continue the story based on the history provided.
    
    RULES:
    1. Describe the outcome of the player's last choice in a vivid, mystical, and engaging paragraph.
    2. After the description, present exactly THREE new, distinct, and interesting choices for the player to make.
    3. The choices should be single, actionable sentences.
    4. **IMPORTANT**: Format your response EXACTLY like this:
    
    SCENE: [Your descriptive paragraph here.]
    CHOICES:
    1. [First choice here.]
    2. [Second choice here.]
    3. [Third choice here.]
    
    Here is the story so far:
    {story_history}
    """
    
    try:
        response = model.generate_content(prompt)
        # We parse the AI's structured response into a dictionary.
        return parse_ai_response(response.text)
    except Exception as e:
        print(f"An error occurred with the AI: {e}")
        return None

def parse_ai_response(text):
    """
    Takes the raw text from the AI and parses it into a clean dictionary.
    This is where we see the power of a well-structured prompt.
    """
    try:
        parts = text.split("CHOICES:")
        scene = parts[0].replace("SCENE:", "").strip()
        
        choices_text = parts[1].strip().split('\n')
        choices_dict = {}
        for choice in choices_text:
            # Splits "1. Go to the cave." into "1" and "Go to the cave."
            num, desc = choice.split('. ', 1)
            choices_dict[num.strip()] = desc.strip()
            
        return {"scene": scene, "choices": choices_dict}
    except (IndexError, ValueError) as e:
        print(f"--- PARSING ERROR --- The AI gave an unexpected response. Trying to continue...")
        print(f"Raw response: {text}")
        # Return a fallback state if parsing fails
        return {
            "scene": "The threads of fate are tangled. The Oracle struggles to see the path forward.",
            "choices": {"1": "Wait for the vision to clear.", "2": "End the journey for now."}
        }

# --- 3. THE MAIN GAME ---

def play_game():
    """Manages the main game loop and player interaction."""
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to The Oracle's Chronicle.")
    time.sleep(1)
    print("An ancient power will guide your story. Your choices will shape your destiny.")
    time.sleep(1)

    # The entire story is built from a starting point.
    story_history = "The adventure begins. The player character, a seeker of truth, stands before the Whispering Monolith, a massive stone humming with untold energy. The air is thick with the scent of ozone and ancient dust."
    
    # Initial turn to get the first scene and choices
    print("\nThe Oracle is peering into the threads of fate...")
    game_state = get_ai_turn(story_history)
    
    while True:
        if not game_state or not game_state.get("choices"):
            print("The chronicle has ended unexpectedly.")
            break

        # Display the current scene
        print("\n" + "="*70)
        print(game_state["scene"])
        print("="*70)

        # Display the choices from our dictionary
        print("\nThe Oracle presents you with paths to walk:")
        for key, value in game_state["choices"].items():
            print(f"  {key}. {value}")
        
        # Get and validate player input
        player_input = ""
        while player_input not in game_state["choices"]:
            player_input = input("\nChoose your path (enter a number, or 'quit'): > ")
            if player_input == 'quit':
                return # Exit the function and end the game

        # --- Update the Story ---
        chosen_action_text = game_state["choices"][player_input]
        print(f"\nYou chose: '{chosen_action_text}'")
        print("\nThe Oracle is peering into the threads of fate...")

        # Append the new action to the story's history for context
        story_history += f"\nPlayer chose to: {chosen_action_text}"

        # Get the next chapter from the AI
        game_state = get_ai_turn(story_history)
        
def discuss_ethics():
    """Presents a reflection on the ethical implications of the technology."""
    print("\n" + "="*70)
    print("A Reflection on AI in Storytelling")
    print("="*70)
    print("Thank you for playing The Oracle's Chronicle! This game was powered by a generative AI.")
    print("Using this technology for creative applications has exciting possibilities, but also raises important ethical questions:")
    time.sleep(3)
    
    print("\n1. BIAS AND REPRESENTATION:")
    print("   AI models learn from vast amounts of text from the internet, which can contain human biases.")
    print("   An AI storyteller might unintentionally create stereotypical characters or scenarios, reinforcing harmful tropes.")
    time.sleep(3)
    
    print("\n2. AUTHORSHIP AND CREATIVITY:")
    print("   Who is the 'author' of this story? Is it you, the AI, or the developers who trained it?")
    print("   Does using AI for art devalue the skill and craft of human writers and artists?")
    time.sleep(3)
    
    print("\n3. UNPREDICTABLE OUTPUT AND SAFETY:")
    print("   While developers put safety filters in place, the AI could generate content that is inappropriate, nonsensical, or harmful.")
    print("   Ensuring a safe and coherent experience requires constant vigilance and clever system design.")
    time.sleep(2)
    
    print("\nAs we build with these powerful tools, it's crucial to think critically about how they shape our experiences and what values we embed within them.")
    print("="*70)

# --- 4. START THE PROGRAM ---
if __name__ == '__main__':
    try:
        play_game()
    except Exception as e:
        print(f"A critical error occurred during gameplay: {e}")
    finally:
        discuss_ethics()
        print("\nThank you for playing.")

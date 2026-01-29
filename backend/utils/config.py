# utils/config.py

import os

def load_system_prompt():
    try:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        prompt_path = os.path.join(base_dir, "prompt.txt")

        with open(prompt_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content.strip()

    except FileNotFoundError:
        raise FileNotFoundError("prompt.txt file not found.")
    except Exception as e:
        raise RuntimeError(f"Error loading system prompt: {e}")

def get_system_prompt():
    return load_system_prompt()

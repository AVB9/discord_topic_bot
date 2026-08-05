import json
import random
from pathlib import Path

# Resolve paths dynamically so the script can be run from anywhere
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
TOPICS_FILE = DATA_DIR / "topics.json"
SENT_TOPICS_FILE = DATA_DIR / "sent_topics.json"

def load_json(file_path: Path) -> list:
    """Loads a JSON list from a file, returning an empty list if it doesn't exist."""
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_json(data: list, file_path: Path) -> None:
    """Saves a list back to a JSON file."""
    # Ensure the directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_daily_topic() -> str:
    """Selects a topic, moves it to the sent list, and saves state."""
    available_topics = load_json(TOPICS_FILE)
    sent_topics = load_json(SENT_TOPICS_FILE)

    # Automatically reset if all topics have been used
    if not available_topics:
        if not sent_topics:
            raise ValueError("No topics found in data/topics.json. Please add topics.")
        
        print("All topics exhausted. Resetting the list from sent_topics.json.")
        available_topics = sent_topics
        sent_topics = []

    # Select a random topic
    selected_topic = random.choice(available_topics)

    # Move the topic to prevent duplication
    available_topics.remove(selected_topic)
    sent_topics.append(selected_topic)

    # Save the new state to the files
    save_json(available_topics, TOPICS_FILE)
    save_json(sent_topics, SENT_TOPICS_FILE)

    return selected_topic
import os
import sys
from src.topic_manager import get_daily_topic
from src.webhook_sender import send_discord_ping

# Try to load local variables from a .env file if running locally
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def main():
    # 1. Retrieve the Discord Webhook URL from the environment
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("Fatal Error: DISCORD_WEBHOOK_URL environment variable is missing.")
        sys.exit(1)

    # 2. Select today's topic and update the JSON trackers
    try:
        topic = get_daily_topic()
        print(f"Topic selected: {topic}")
    except Exception as e:
        print(f"Topic Manager Error: {e}")
        sys.exit(1)

    # 3. Post the message to Discord
    try:
        send_discord_ping(webhook_url, topic)
        print("Success: Daily ping sent to Discord.")
    except Exception as e:
        print(f"Webhook Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
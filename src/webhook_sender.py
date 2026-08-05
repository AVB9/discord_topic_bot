import requests

def send_discord_ping(webhook_url: str, topic: str) -> None:
    payload = {
        "content": (
            "@everyone Good morning.\n\n"
            f"**Today's Topic:** {topic}\n\n"
            "Think on this during the day. We will meet in the voice channel tonight to discuss."
        )
    }
    response = requests.post(webhook_url, json=payload)
    response.raise_for_status()
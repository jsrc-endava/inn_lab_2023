import os
import requests

class NoahCoreService:
  def __init__(self):
    self.api_url = os.environ.get('NOAH_CORE_API_URL')

  def save_message(self, slack_data):
    payload = {
      "message_id": slack_data["ts"],
      "channel_id": slack_data["channel"],
      "user_id": slack_data["user"],
      "team_id": slack_data["team"],
      "username": "",
      "text": slack_data["text"]
    }

    response = requests.post(f"{self.api_url}/slack/save_message", json=payload)
    print(response)



from noah_core.models.slack_message import SlackMessage
from noah_core.extensions import db

def save_message(message_id, channel_id, user_id, team_id, username, text):
  print("Saving message")
  message = SlackMessage(
    message_id=message_id, channel_id=channel_id, user_id=user_id, team_id=team_id, username=username, text=text
  )
  db.session.add(message)
  db.session.commit()
  db.session.refresh(message)
  return message

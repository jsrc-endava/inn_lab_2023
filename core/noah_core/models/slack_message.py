from dataclasses import dataclass
from noah_core.extensions import db

@dataclass
class SlackMessage(db.Model):
  __tablename__ = 'slack_messages'

  # dataclass fields to serialize
  id: int
  message_id: str
  channel_id: str
  user_id: str
  team_id: str
  username: str
  text: str

  # db fields
  id = db.Column(db.Integer, primary_key=True)
  message_id = db.Column(db.String(50), nullable=False)
  channel_id = db.Column(db.String(50))
  user_id = db.Column(db.String(50))
  team_id = db.Column(db.String(50))
  username = db.Column(db.String(50))
  text = db.Column(db.Unicode(500), nullable=False)

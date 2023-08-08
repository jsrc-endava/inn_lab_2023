from flask import Blueprint, request, jsonify
from .helpers import messages_helper

def slack_blueprint():
  bp = Blueprint('slack', __name__, url_prefix='/slack')

  @bp.route('/save_message', methods=['POST'])
  def save_slack_message():
    data = request.get_json()
    print(data)
    message = messages_helper.process_message(
      message_id=data.get('message_id'),
      channel_id=data.get('channel_id'),
      user_id=data.get('user_id'),
      team_id=data.get('team_id'),
      username=data.get('username'),
      text=data.get('text')
    )
    return jsonify(message)
  
  return bp

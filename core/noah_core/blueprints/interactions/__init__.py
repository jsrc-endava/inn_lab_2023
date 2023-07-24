from flask import Blueprint, request
from .information_extraction import answers

def interactions_blueprint():
  bp = Blueprint('interactions', __name__, url_prefix='/interactions')

  @bp.route('/answer_question', methods=['POST'])
  def answer_question():
    data = request.get_json()
    return answers.answer(data["query"])
  
  return bp

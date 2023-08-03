from noah_core.blueprints.slack.helpers.messages_helper import MessagesHelper
from noah_core.models.slack_message import SlackMessage

class TestMessageHelpers:
  def test_save_message(self, session):
    helper = MessagesHelper()
    model = SlackMessage()

    session.add(model)

    print(model)
    print(helper.save_message("test"))

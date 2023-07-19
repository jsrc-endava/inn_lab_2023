import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

load_dotenv('.env')

# Initializes your app with your bot token and signing secret
app = App(
  token=os.environ.get("SLACK_BOT_TOKEN"),
  signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
app_handler = SlackRequestHandler(app)


@app.event("message")
def handle_message(message, say, logger):
  logger.info("Handling message")
  logger.info(message)
  print("Handling message")
  print(message)

api = FastAPI()


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)

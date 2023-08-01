import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

load_dotenv('.env')

app = App()
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


@api.get("/slack/install")
async def install(req: Request):
  print(await req.body())
  return await app_handler.handle(req)


@api.get("/slack/oauth_redirect")
async def oauth_redirect(req: Request):
  return await app_handler.handle(req)

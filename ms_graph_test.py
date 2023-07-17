import os
from dotenv import load_dotenv
import asyncio
from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient


load_dotenv('.env')

# The client credentials flow requires that you request the
# /.default scope, and pre-configure your permissions on the
# app registration in Azure. An administrator must grant consent
# to those permissions beforehand.
scopes = [
  'api://44f23afb-477d-4a9a-a96b-d43df67e7b85/.default'
]

# Multi-tenant apps can use "common",
# single-tenant apps must use the tenant ID from the Azure portal
# Values from app registration
tenant_id = os.environ['AZURE_TENANT_ID']
client_id = os.environ['AZURE_CLIENT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']

# azure.identity.aio
credential = ClientSecretCredential(
  tenant_id=tenant_id,
  client_id=client_id,
  client_secret=client_secret
)

graph_client = GraphServiceClient(credential, scopes)

async def messages():
  return await graph_client.chats.by_chat_id('91e0480577ac491bb1b853c4d7a02ee0').get()

asyncio.run(messages())

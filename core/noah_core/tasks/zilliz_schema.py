from invoke import task

import os
from dotenv import load_dotenv
from pymilvus import MilvusClient, FieldSchema, CollectionSchema, DataType

load_dotenv('.env')

ZILLIZ_ENDPOINT = os.environ['ZILLIZ_ENDPOINT']
ZILLIZ_TOKEN = os.environ['ZILLIZ_TOKEN']

MESSAGES_EMBEDDINGS_FIELDS = [
  FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=True),
  FieldSchema(name="message_id", dtype=DataType.INT64),
  FieldSchema(name="source", dtype=DataType.VARCHAR, max_length=512),
  FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=8192),
  FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=1536),
]

EMBEDDINGS_INDEX = {
  "field_name": "vector",
  "index_type": "AUTOINDEX",
  "metric_type": "L2",
  "params": {}
}

class CreateZillizSchema():
  def __init__(self, zilliz_client=MilvusClient(uri=ZILLIZ_ENDPOINT, token=ZILLIZ_TOKEN)):
    self.zilliz_client = zilliz_client

  def create_schema(self):
    self.zilliz_client.drop_collection("messages")
    self.zilliz_client.create_collection_with_schema(
      "messages", 
      CollectionSchema(MESSAGES_EMBEDDINGS_FIELDS, "Message Embeddings", enable_dynamic_field=False),
      EMBEDDINGS_INDEX
    )

  def run(self):
    self.create_schema()

@task
def messages(c):
  CreateZillizSchema().run()

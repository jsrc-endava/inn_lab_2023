import os
from dotenv import load_dotenv
from pymilvus import MilvusClient, FieldSchema, CollectionSchema, DataType
from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv('.env')

# Vector databases:
# In this example we are using Milvus
zilliz_client=MilvusClient(
  uri=os.environ['ZILLIZ_ENDPOINT'],
  token=os.environ['ZILLIZ_TOKEN']
)
zilliz_client.drop_collection("innovation_lab")
zilliz_client.create_collection_with_schema(
  "innovation_lab", 
  CollectionSchema(
    [
      FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=True),
      FieldSchema(name="some_id", dtype=DataType.INT64),
      FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=8192),
      FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=1536),
    ], 
    "Example for synaptron workshop",
    enable_dynamic_field=False
  ),
  {
    "field_name": "vector",
    "index_type": "AUTOINDEX",
    "metric_type": "L2",
    "params": {}
  }
)

from invoke import task

import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus

load_dotenv('.env')

ZILLIZ_ENDPOINT = os.environ['ZILLIZ_ENDPOINT']
ZILLIZ_TOKEN = os.environ['ZILLIZ_TOKEN']

@task
def messages(c):
  loader = TextLoader("./state_of_the_union.txt")
  documents = loader.load()
  text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
  texts = text_splitter.split_documents(documents)

  docsearch = Milvus.from_documents(
    texts,
    embedding=OpenAIEmbeddings(),
    collection_name="messages",
    connection_args={
      "uri": os.environ['ZILLIZ_ENDPOINT'],
      "token": os.environ['ZILLIZ_TOKEN'],
    },
  )

  print(docsearch)

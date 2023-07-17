import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus

load_dotenv('.env')

loader = TextLoader("./workshop/langchain/state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

docsearch = Milvus.from_documents(
  texts,
  embedding=OpenAIEmbeddings(),
  collection_name="innovation_lab_docsearch",
  connection_args={
    "uri": os.environ['ZILLIZ_ENDPOINT'],
    "token": os.environ['ZILLIZ_TOKEN'],
  },
)

qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())

query = "How many adult Americans are fully vaccinated?"
print(qa.run(query))

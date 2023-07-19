import os
from dotenv import load_dotenv
import openai

load_dotenv('.env')

openai.api_key = os.environ['OPENAI_API_KEY']

prompt = """
Based on the context

{context}

Who is Nicola Tesla?"""

# create a completion
completion = openai.Completion.create(
    prompt=prompt,
    temperature=1,
    max_tokens=600,
    model="text-davinci-003",
)

print("Completion")
print(completion)

# create a chat completion
chat_completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "Who is Nicola Tesla!"}]
)

print("Chat completion")
print(chat_completion)

<<<<<<< HEAD
from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure OpenAI service client 
client = OpenAI()

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-3.5-turbo"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
=======
from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure OpenAI service client 
client = OpenAI()
deployment = "gpt-3.5-turbo"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
>>>>>>> b88b09e22d023505eb4b289b4b85fe9f42c33293

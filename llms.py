from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
SERVICE_KEY = os.getenv('OPEN_API_KEY')

llm = OpenAI(openai_api_key=SERVICE_KEY, model_name="gpt-3.5-turbo-1106")
chat = ChatOpenAI(openai_api_key=SERVICE_KEY)

a = llm.predict("How many planets are there?")
b = chat.predict("How many planets are there?")

print(a)

print(b)
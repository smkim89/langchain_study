from langchain.llms.openai import OpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()
SERVICE_KEY = os.getenv('OPEN_API_KEY')

llm = OpenAI(openai_api_key=SERVICE_KEY, model_name="gpt-3.5-turbo-1106", temperature=0.9)
#prompt 를 여러가지 지정해서 보낼수있음. 배경, ai의 기본 설명, 그리고 질문에대한 분리
messages = [
    SystemMessage(content = "You Are a geography expert. and you only reply in Korean"),
    AIMessage(content="안녕 나는 SMBOT이야!!"),
    HumanMessage(content = "What is the distance between Maxico And Thailand. Also, What is your name?")
]

aiMsg = llm.predict_messages(messages)


print(aiMsg)
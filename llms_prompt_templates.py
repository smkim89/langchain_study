from langchain.llms.openai import OpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
SERVICE_KEY = os.getenv('OPEN_API_KEY')

llm = OpenAI(openai_api_key=SERVICE_KEY, model_name="gpt-3.5-turbo-1106", temperature=0.1)

template = PromptTemplate.from_template("What is the distance between {country_a} And {country_b}")

prompt = template.format(country_a="Maxico", country_b="Korea")

template2 = ChatPromptTemplate.from_messages([
    ("system", "You Are a geography expert. and you only reply in {language}."),
    ("ai", "안녕 나는 {name}이야!!"),
    ("human", "What is the distance between {country_a} And {country_b}. Also, What is your name?")
]
)

promt2 = template2.format_messages(
    language="English",
    name="SAM",
    country_a="Korea",
    country_b="Japan"
)

print(promt2)
reply = llm.predict_messages(promt2)
print(reply)
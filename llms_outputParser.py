from langchain.llms.openai import OpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os

class CommaOutputParser(BaseOutputParser):

    def parse(self, text):
        return text.strip().split(",")



p = CommaOutputParser()
p.parse("Hello, how, are, you")

load_dotenv()
SERVICE_KEY = os.getenv('OPEN_API_KEY')

llm = OpenAI(openai_api_key=SERVICE_KEY, model_name="gpt-3.5-turbo-1106", temperature=0.1)


template = ChatPromptTemplate.from_messages([
    ("system", "you are a list generation machine. Everthing you are asked will be answered whit a list of max {max_items}. Do not reply will anything else. Everythins is lowercase"),
    ("human", "{question}")
])

prompt = template.format_messages(max_items=10, question="What are the colors?");
reply = llm.predict_messages(prompt)
p.parse(reply.content)

# Template | chat | outputParser() 의 형태로 체인을 엮을수 있음 예로  chain끼리도 묶을수 있음.
# chain = template | llm | CommaOutputParser()
# chain2 = template_2 | llm2 | outputParser()
# all = chain | chain2 | outputparser()

chain = template | llm | CommaOutputParser()
reply2 = chain.invoke({
    "max_items": 10,
    "question": "What are the pokemons??"
})


print(reply2)
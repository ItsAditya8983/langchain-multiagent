from langchain.agents import create_agent   # here we havent imported create_react_agent because in newer version it is replaced as create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search, scrape_url
from dotenv import load_dotenv
import os



# in this newer version of langchain we dont have to implement agentexecutor because it is already in this version 

load_dotenv()

# Model initialization
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0.0,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
# Creating first Agent for web search 

def create_web_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        
    )   

# creating second Agent for web scraping named as reader agent 

def create_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
        
    )



#writer chain 

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()


#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
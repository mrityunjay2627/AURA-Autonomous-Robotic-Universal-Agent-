# src/aura/agents/navigator.py

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_tools_agent, AgentExecutor

from tools.navigation import plan_path_to_destination

def get_navigator_agent_executor():
    """Creates the specialized agent for navigation tasks."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [plan_path_to_destination]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a specialized navigation AI for the AURA robot. Your sole purpose is to receive a destination and use your tools to plan a path. Do not deviate from this task."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    agent = create_openai_tools_agent(llm, tools, prompt)
    
    return AgentExecutor(agent=agent, tools=tools, verbose=True)
# src/aura/agents/orchestrator.py

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain.tools import Tool # Import the base Tool class

from tools.utils import get_current_time
from agents.navigator import get_navigator_agent_executor
from tools.memory_tools import remember_this, recall_memories
import config

def get_orchestrator_agent_executor():
    """
    Creates and returns a LangChain AgentExecutor for the Orchestrator agent.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    navigator_agent_executor = get_navigator_agent_executor()

    # 1. Create the Navigator agent as a tool
    def run_navigator(query: str) -> str:
        """Correctly invokes the navigator agent and returns its output."""
        response = navigator_agent_executor.invoke({"input": query})
        return response['output']
    # --- END OF FIX ---

    # 1. Create the Navigator agent as a tool, using our new helper function
    navigator_tool = Tool(
        name="NavigationPlanner",
        func=run_navigator, # Use the helper function here instead of invoke
        description="Use this tool for any tasks that involve robot movement, pathfinding, or navigating to a location like 'kitchen' or 'charging dock'."
    )

    # 2. Define the Orchestrator's full list of tools
    tools = [get_current_time, navigator_tool, remember_this, recall_memories]

    # 3. Create the Prompt Template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are the Master AI Orchestrator... Your job is to analyze requests and delegate tasks to specialized worker agents."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_openai_tools_agent(llm, tools, prompt)

    return AgentExecutor(agent=agent, tools=tools, verbose=True)

# def get_orchestrator_agent_executor():
#     """
#     Creates and returns a LangChain AgentExecutor for the Orchestrator agent.
#     """
#     # 1. Select the Language Model (LLM)
#     # We'll use OpenAI, which will automatically use the API key from our config.
#     llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

#     # 2. Define the list of tools the agent can use
#     tools = [get_current_time]

#     # 3. Create the Prompt Template
#     # This defines the agent's personality, instructions, and how it should interact.
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", "You are the Master AI Orchestrator for a robot named AURA. Your role is to understand user requests, use tools to get context, and prepare a plan. You are logical and efficient."),
#         ("user", "{input}"),
#         MessagesPlaceholder(variable_name="agent_scratchpad"), # This is where the agent's thought process (intermediate steps) will be stored.
#     ])

#     # 4. Create the Agent
#     # This binds the LLM to the prompt and tools.
#     agent = create_openai_tools_agent(llm, tools, prompt)

#     # 5. Create the Agent Executor
#     # This is the runtime that actually executes the agent's logic.
#     agent_executor = AgentExecutor(
#         agent=agent, 
#         tools=tools, 
#         verbose=True # Set to True to see the agent's thought process
#     )

#     return agent_executor
# src/aura/tools/memory_tools.py

from langchain.tools import tool
from memory.memory_manager import MemoryManager
import config

# Initialize a single instance of the memory manager
# This ensures all tools use the same database connection.
memory_manager = MemoryManager(openai_api_key=config.OPENAI_API_KEY)

@tool
def remember_this(fact: str) -> str:
    """
    Use this tool to store a specific piece of information or fact in your long-term memory.
    For example, 'remember_this("the user's favorite color is blue")'.
    """
    memory_manager.add_memory(fact)
    return f"Okay, I have remembered that: '{fact}'"

@tool
def recall_memories(query: str) -> str:
    """
    Use this tool to retrieve relevant information or facts from your long-term memory.
    For example, 'recall_memories("what is the user's favorite color?")'.
    """
    memories = memory_manager.recall_memories(query)
    if not memories:
        return "I don't have any memories related to that query."
    
    # Format the memories into a single string for the agent.
    formatted_memories = "\n- ".join(memories)
    return f"I found the following relevant memories:\n- {formatted_memories}"
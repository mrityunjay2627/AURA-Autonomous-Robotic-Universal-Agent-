# src/aura/tools/navigation.py

from langchain.tools import tool

@tool
def plan_path_to_destination(destination: str) -> str:
    """
    Calculates and returns a planned path to a specified destination within the house.
    Use this tool for any requests involving movement or navigation.
    """
    print(f"🤖 NAVIGATOR TOOL: Planning path to {destination}...")
    # In a real robot, this would call a complex pathfinding algorithm (e.g., A*).
    # For now, we simulate success.
    return f"Path to '{destination}' has been successfully planned. The robot can now proceed."
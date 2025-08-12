# src/aura/tools/utils.py

from datetime import datetime
from langchain.tools import tool # Import the decorator

@tool
def get_current_time() -> str:
    """
    Returns the current date and time. Use this tool to get the current timestamp
    for any requests or logs. The location is Tempe, Arizona.
    """
    return f"The current date and time in Tempe, Arizona is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
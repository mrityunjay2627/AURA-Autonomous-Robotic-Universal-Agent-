# src/aura/main.py
import time

import config
from agents.orchestrator import get_orchestrator_agent_executor

def run_aura():
    """
    Main function to initialize and run the AURA agent system.
    """
    print("Initializing AURA...")

    # We can verify that the config is loaded correctly
    if not config.OPENAI_API_KEY:
        print("ERROR: OpenAI API key not found. Check your .env file.")
        return

    print("AURA system is ready. Awaiting instructions...")
    # In the future, this is where we'll start the main agent loop.
    print("-" * 50)

    # Get our runnable agent
    aura_agent_executor = get_orchestrator_agent_executor()
    
    # # Give a sample instruction that requires navigation
    # # user_instruction = "First, tell me the time, and then figure out how to get to the charging dock."
    # user_instruction = "Please remember that my name is Priyanshu M Sharma. Then, tell me what you just remembered."
    
    # result = aura_agent_executor.invoke({"input": user_instruction})
    
    # print("\n" + "-" * 50)
    # print("Orchestrator execution finished. Final Answer:")
    # print(result["output"])
    while True:
        print("--- Starting new execution cycle ---")
        user_instruction = "My name is Sam, please remember that. Then, tell me my name."
        
        try:
            result = aura_agent_executor.invoke({"input": user_instruction})
            print("Orchestrator execution finished. Final Answer:")
            print(result["output"])
        except Exception as e:
            print(f"An error occurred during agent execution: {e}")

        print("--- Execution cycle finished. Waiting for 60 seconds... ---")
        time.sleep(60) # This keeps the process alive.

if __name__ == "__main__":
    run_aura()
# src/aura/main.py
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
    
    # Give a sample instruction that requires navigation
    # user_instruction = "First, tell me the time, and then figure out how to get to the charging dock."
    user_instruction = "Please remember that my name is Priyanshu M Sharma. Then, tell me what you just remembered."
    
    result = aura_agent_executor.invoke({"input": user_instruction})
    
    print("\n" + "-" * 50)
    print("Orchestrator execution finished. Final Answer:")
    print(result["output"])

if __name__ == "__main__":
    run_aura()
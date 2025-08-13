# src/aura/memory/memory_manager.py

import chromadb
from chromadb.utils import embedding_functions
from datetime import datetime # <-- Add this import at the top of the file

class MemoryManager:
    # ... (the __init__ function remains exactly the same) ...
    def __init__(self, openai_api_key: str):
        self.client = chromadb.PersistentClient(path="./aura_memory")
        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=openai_api_key,
            model_name="text-embedding-3-small"
        )
        self.collection = self.client.get_or_create_collection(
            name="aura_knowledge",
            embedding_function=self.embedding_function
        )
        print("Memory Manager initialized with ChromaDB.")

    # --- THIS IS THE CORRECTED FUNCTION ---
    def add_memory(self, fact: str, metadata: dict = None):
        """Adds a piece of text (a memory) to the database."""
        doc_id = str(hash(fact))

        # Create a base metadata dict that is never empty.
        current_metadata = {"timestamp": datetime.now().isoformat()}

        # If the user provides additional metadata, merge it in.
        if metadata:
            current_metadata.update(metadata)

        self.collection.add(
            documents=[fact],
            ids=[doc_id],
            metadatas=[current_metadata] # Pass the guaranteed non-empty dict
        )
        print(f"Memory added: '{fact}'")
    # --- END OF FIX ---

    # ... (the recall_memories function remains exactly the same) ...
    def recall_memories(self, query: str, num_results: int = 2) -> list[str]:
        results = self.collection.query(
            query_texts=[query],
            n_results=num_results
        )
        return results['documents'][0] if results and results['documents'] else []
import os
from dotenv import load_dotenv
import vertexai
from vertexai.preview import rag

load_dotenv()

def initialize_rag():
    project = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")
    
    if not project or not location:
        print("Error: Please set GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION in .env first.")
        return

    vertexai.init(project=project, location=location)

    # Create the permanent storage for your documents
    print(f"Creating RAG Corpus in {location}...")
    corpus = rag.create_corpus(
        display_name="my_rag_knowledge_base",
        description="One-time setup for my RAG agent storage"
    )
    
    # Extract the ID from the full resource name
    corpus_id = corpus.name.split('/')[-1]
    
    print("\n--- SETUP COMPLETE ---")
    print(f"Full Resource Name: {corpus.name}")
    print(f"Add this to your .env file:")
    print(f"RAG_CORPUS_ID={corpus_id}")

if __name__ == "__main__":
    initialize_rag()
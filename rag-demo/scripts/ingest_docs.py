import os
from dotenv import load_dotenv
import vertexai
from vertexai.preview import rag

# Load your .env (including the CORPUS_ID you just found)
load_dotenv()

def ingest_data():
    project = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")
    corpus_id = os.getenv("RAG_CORPUS_ID")
    
    # Construct the full resource name
    corpus_name = f"projects/{project}/locations/{location}/ragCorpora/{corpus_id}"

    vertexai.init(project=project, location=location)

    # Path to your local file
    file_path = "data/file.pdf" 
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}. Please create a 'data' folder and add a file.")
        return

    print(f"Uploading {file_path} to Corpus {corpus_id}...")
    
    # upload_file is a synchronous call (it waits until the upload is done)
    rag_file = rag.upload_file(
        corpus_name=corpus_name,
        path=file_path,
        display_name="Project Manual",
        description="Technical documentation for the RAG agent"
    )

    print(f"Successfully uploaded! File ID: {rag_file.name}")

if __name__ == "__main__":
    ingest_data()
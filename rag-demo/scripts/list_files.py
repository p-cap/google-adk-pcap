# Add this to a new file 'list_files.py'
import os
from dotenv import load_dotenv
import vertexai
from vertexai.preview import rag

load_dotenv()
vertexai.init(project=os.getenv("GOOGLE_CLOUD_PROJECT"), location=os.getenv("GOOGLE_CLOUD_LOCATION"))

corpus_name = f"projects/{os.getenv('GOOGLE_CLOUD_PROJECT')}/locations/{os.getenv('GOOGLE_CLOUD_LOCATION')}/ragCorpora/{os.getenv('RAG_CORPUS_ID')}"
files = rag.list_files(corpus_name=corpus_name)

for f in files:
    print(f"File: {f.display_name} | ID: {f.name}")
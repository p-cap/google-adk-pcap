import os
from dotenv import load_dotenv
import vertexai
from vertexai.preview import rag

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

# List all corpora in your project/location
corpora = rag.list_corpora()

print("\n--- Your Available Corpora ---")
for corpus in corpora:
    # The name looks like: projects/123/locations/us-central1/ragCorpora/456789
    corpus_id = corpus.name.split('/')[-1]
    print(f"Display Name: {corpus.display_name}")
    print(f"CORPUS_ID:    {corpus_id}")
    print("-" * 30)
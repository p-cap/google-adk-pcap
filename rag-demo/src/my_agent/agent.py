import asyncio
import os
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.apps import App
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval

# NEW: Import types for structured messages
from google.genai import types 
import vertexai
from vertexai.preview import rag
import uuid 

load_dotenv()


# Configuration constants
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
CORPUS_ID = os.getenv("RAG_CORPUS_ID")
CORPUS_PATH = f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{CORPUS_ID}"

vertexai.init(project=PROJECT_ID, location=LOCATION)

rag_tool = VertexAiRagRetrieval(
    name="document_retrieval",
    description="Search through my uploaded PDF documents.",
    rag_resources=[rag.RagResource(rag_corpus=CORPUS_PATH)]
)

rag_agent = LlmAgent(
    name="research_assistant",
    model="gemini-2.5-flash",
    tools=[rag_tool],
    instruction="Use the document_retrieval tool to answer questions."
)

RAG_APP_NAME="rag_knowledge_app"
rag_app = App(name=RAG_APP_NAME, root_agent=rag_agent)

async def get_ai_response(runner, user_text, user_id, session_id):
    user_message = types.Content(
        role="user",
        parts=[types.Part(text=user_text)]
    )
    
    async for event in runner.run_async(
        new_message=user_message,
        user_id=user_id,
        session_id=session_id  
    ):
        # FIX: Check if event.content exists BEFORE accessing .parts
        if event.is_final_response() and event.content and event.content.parts:
            # Use .text attribute directly if available on the parts object
            return event.content.parts[0].text
            
    return "Agent completed without a text response."

async def chat():
    USER_ID = "local_dev_user"
    session_id = str(uuid.uuid4())
    my_session_service = InMemorySessionService()
    runner = Runner(app=rag_app, session_service=my_session_service)
    print(f"\n--- 🤖 RAG Agent Ready ---")
    session_id = str(uuid.uuid4())
    await my_session_service.create_session(
        session_id=session_id,
        app_name=RAG_APP_NAME,
        user_id=USER_ID
        )
    while True:
        print("++++ Welcome to p-cap's RAG demo ++++")
        print('[To exit, type "exit"]')
        query = input("User: ").strip()
        if query.lower() in ["exit", "quit"]: break
        if not query: continue

        print("Thinking...")
        response = await get_ai_response(runner, query, USER_ID, session_id)
        print(f"\nAI: {response}\n")

if __name__ == "__main__":
    asyncio.run(chat())
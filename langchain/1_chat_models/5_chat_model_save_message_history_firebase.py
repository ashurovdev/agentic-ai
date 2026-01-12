# Example Source: https://python.langchain.com/v0.2/docs/integrations/memory/google_firestore/

from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import AzureChatOpenAI
import os

"""
Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project and copy the Project ID
3. Create a Firestore database in the Firebase project
4. Install the Google Cloud CLI
    - Authenticate the CLI with your Google account
    - Set default project to your Firebase project
5. Enable Firestore API in the Google Cloud Console
"""

# Load environment variables
load_dotenv()

# -------------------- Firestore Setup --------------------
PROJECT_ID = "langchain-demo-abf48"
SESSION_ID = "user_session_new"  # username or unique ID
COLLECTION_NAME = "chat_history"

print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# -------------------- Azure OpenAI Model --------------------
model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
)

# -------------------- Chat Loop --------------------
print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    # Add user message to Firestore
    chat_history.add_user_message(human_input)

    # Invoke Azure OpenAI model
    ai_response = model.invoke(chat_history.messages)

    # Add AI message to Firestore
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")


import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

load_dotenv()

service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
api_key = os.getenv("AZURE_SEARCH_API_KEY")

search_client = SearchClient(
    endpoint=service_endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(api_key),
)

def az_ai_retrieve(query: str) -> str:
    results = search_client.search(search_text=query)

    text = ""
    for result in results:
        title = result.get("title", "unknown")
        chunk = result.get("chunk", "")
        text += f"Source: {title}\nContent: {chunk}\n\n"

    return text

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
import os

# Load environment variables
load_dotenv()

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# ---- Azure OpenAI Chat Model Example ----
model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
)

result = model.invoke(messages)
print(f"Answer from Azure OpenAI: {result.content}")


# ---- Anthropic Chat Model Example ----
# # Anthropic models: https://docs.anthropic.com/en/docs/models-overview
# model = ChatAnthropic(
#     model="claude-3-opus-20240229",
#     api_key=os.getenv("ANTHROPIC_API_KEY"),
# )
#
# result = model.invoke(messages)
# print(f"Answer from Anthropic: {result.content}")
#

# ---- Google Chat Model Example ----
# https://ai.google.dev/gemini-api/docs/models/gemini
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

result = model.invoke(messages)
print(f"Answer from Google: {result.content}")

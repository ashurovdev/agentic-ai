from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
import os

# Load environment variables
load_dotenv()

# Create Azure Chat model
model = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
)

# PART 1: Prompt from Template
print("----- Prompt from Template -----")
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic": "cats"})
result = model.invoke(prompt)
print(result.content)

# PART 2: Prompt with Multiple Placeholders
print("\n----- Prompt with Multiple Placeholders -----\n")
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} short story about a {animal}.
Assistant:"""

prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({
    "adjective": "funny",
    "animal": "panda"
})

result = model.invoke(prompt)
print(result.content)

# PART 3: Prompt with System and Human Messages
print("\n----- Prompt with System and Human Messages -----\n")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes.")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({
    "topic": "lawyers",
    "joke_count": 3
})

result = model.invoke(prompt)
print(result.content)

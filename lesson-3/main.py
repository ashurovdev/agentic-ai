from google.genai import Client
from google.genai import types

client = Client()


def db_tool(query: str):
    """
    Return user information based on written query
    """
    pass


config = types.GenerateContentConfig(
    tools=[db_tool],
    system_instruction="Always answer with human readable format after tool calling."
)


user_input = "Give me information about user with id 1"


response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=f"""{user_input}""",
    config=config
)

print(response.text)
import os
import json
from dotenv import load_dotenv

from openai_client import client, DEPLOYMENT_NAME
from tools import TOOLS
from azure_search import az_ai_retrieve

load_dotenv()

SYSTEM_PROMPT = (
    "You are a RAG assistant.\n"
    "You MUST always call the provided tool to answer the user's question.\n"
    "When answering, give references to the sources returned by the tool."
)

USER_QUESTION = str(input("Ask a question related to travelling: "))

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": USER_QUESTION},
]

response = client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=messages,
    tools=TOOLS,
    tool_choice="auto",
)

assistant_message = response.choices[0].message
tool_calls = assistant_message.tool_calls or []

if not tool_calls:
    tool_result = az_ai_retrieve(USER_QUESTION)
    messages.append({"role": "assistant", "content": ""})
    messages.append(
        {
            "role": "tool",
            "tool_call_id": "forced",
            "name": "az_ai_retrieve",
            "content": tool_result,
        }
    )
else:
    messages.append(
        {
            "role": "assistant",
            "content": assistant_message.content or "",
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in tool_calls
            ],
        }
    )

    for tc in tool_calls:
        args = json.loads(tc.function.arguments)
        result = az_ai_retrieve(**args)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tc.id,
                "name": tc.function.name,
                "content": result,
            }
        )

final_response = client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=messages,
    tools=TOOLS,
)

print(final_response.choices[0].message.content)

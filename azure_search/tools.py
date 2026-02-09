TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "az_ai_retrieve",
            "description": "Retrieve travel related documents from Azure Cognitive Search",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "User travel question"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

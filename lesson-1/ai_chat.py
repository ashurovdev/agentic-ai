from google import genai
from config import API_KEY
import os

client = genai.Client(api_key=API_KEY)
file_name = "chat_history.txt"

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        history = f.read()
else:
    history = ""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Chat boshlanishi\n\n")

while True:
    user_input = input("Human: ")
    if user_input.lower() == "q":
        print("Chat tugadi.")
        break
    else:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history + f"\nHuman: {user_input}",
        )

        ai_text = response.text
        print(f"AI: {ai_text}")

        history += f"\nHuman: {user_input}\nAI: {ai_text}"

        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"Human: {user_input}\n")
            f.write(f"AI: {ai_text}\n\n")


from google import genai
from google.genai import types
import sqlite3
from config import API_KEY

client = genai.Client(api_key=API_KEY)


DB_FILE = "user.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT
)
""")

cursor.execute("SELECT COUNT(*) FROM customers")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO customers (name, email) VALUES (?, ?)",
        [
            ("Alice", "alice@example.com"),
            ("Bob", "bob@example.com"),
            ("Charlie", "charlie@example.com"),
        ]
    )

conn.commit()
conn.close()

# -----------------------------------------------
def tool_db(query: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in rows] if rows else "No results found."
        else:
            conn.commit()
            return "Query executed successfully."
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()
# ---------------------------------------------------------

config = types.GenerateContentConfig(
    tools=[tool_db],
    system_instruction="""
You are an AI that converts user questions into SQLite SQL queries.
Database schema:

TABLE customers:
- id INTEGER
- name TEXT
- email TEXT

Rules:
- Return ONLY SQL
- Do NOT explain anything
- Use valid SQLite syntax
"""
)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Return info about id 2",
    config=config
)

print(response.text)

from sqlalchemy import create_engine, text
import os

db_path = os.path.join(os.path.dirname(__file__), "school.db")
engine = create_engine(f"sqlite:///{db_path}", echo=False)

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('MySchool')


@mcp.tool()
def db_tool(query: str) -> str:
    """
    Executes SQLite query on local database and returns result
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

            if not rows:
                return "No rows returned"

            return "\n".join(str(row) for row in rows)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    mcp.run(transport='stdio')

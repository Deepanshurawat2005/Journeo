
import os
import asyncio
import certifi
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing from .env")

client = MultiServerMCPClient(
    {
        "tavily": {
            "transport": "streamable_http",
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={TAVILY_API_KEY}",
        }
    }
)

async def get_all_tools():
    tools = await client.get_tools()

    print("Available tools:")
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")


async def tavily_mcp_search(query: str):
    tools = await client.get_tools()

    tavily_search_tool = next(
        (tool for tool in tools if tool.name == "tavily_search"),
        None,
    )

    if tavily_search_tool is None:
        raise ValueError("tavily_search tool is not available")

    results = await tavily_search_tool.ainvoke({"query": query})
    return results

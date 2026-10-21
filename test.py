import asyncio
from mcp_client_test import get_all_tools,tavily_mcp_search


if __name__ == "__main__":
    results = asyncio.run(tavily_mcp_search("tell me about the latest 2 news in AI"))
    print(results)
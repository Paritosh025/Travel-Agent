import os
import asyncio
import certifi
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# this is remote client which will connect to the remote mcp server and we can use it to send requests to the remote mcp server.
client = MultiServerMCPClient( 
    {
       "tavily": {
            "transport": "streamable_http",
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={TAVILY_API_KEY}"
        },
  
    }
)



async def get_all_tools():
    tools = await client.get_tools() # to use await we need to use so we can use it to get all the tools from the remote mcp server.
    print("\nAvailable tools in the remote mcp server:\n")

    for tool in tools:
        print(tool.name)


# This retuns tavily_search tool object
tavily_search_tool = None # initially the value is None. We only need TAvily search tool not all tavily tools.

async def get_tavily_search_tool():
    global tavily_search_tool
    if tavily_search_tool is not None:
        return

    tools = await client.get_tools() # to use await we need to use so we can use it to get all the tools from the remote mcp server.
    print("\nAvailable MCP Tools:")

    for tool in tools: # loop through all the tools and print their names
        print(tool.name)

    tavily_search_tool = next( # this will return the first tool which has name tavily_search and assign it to tavily_search_
        tool
        for tool in tools
        if tool.name == "tavily_search"
    )


# This function can be used to call the tavily_search tool with a query in backend.py
async def tavily_mcp_search(query: str):
    await get_tavily_search_tool()
    result = await tavily_search_tool.ainvoke( # first to call the tavily_search tool we need to get the tool object and then we can call the tool with the query.
        {
            "query": query # scores in football
        }
    )
    return result
    # print(result)

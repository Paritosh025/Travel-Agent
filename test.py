import asyncio
from mcp_client import get_all_tools


if __name__ == "__main__":
    query = "Latest news about AI in Nov 2026"
    asyncio.run(get_all_tools())

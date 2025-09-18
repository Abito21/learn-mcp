import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

load_dotenv()


async def main():
    firecrawl_api_key = os.environ.get("FIRECRAWL_API_KEY")

    if not firecrawl_api_key:
        print("Error: FIRECRAWL_API_KEY tidak ditemukan di file .env")
        return
    async with MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": firecrawl_api_key
        }
    }
    ) as server, MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": firecrawl_api_key
        }
    }
    ) as server2 :
        agent = Agent(
            "Assistant",
            instructions="You are a helpful assistant",
            model="gpt-4.1",
            mcp_servers=[server, server2],
        )
        runner = await Runner.run(agent, input="Open Puppeteer, go to abidportfolio-web.vercel.app, and scrape the content!")
        print(runner.final_output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

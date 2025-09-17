from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

load_dotenv()


async def main():
    async with MCPServerStdio(
        params={
            "command": "npx",
            "args": [
              "-y",
              "@modelcontextprotocol/server-puppeteer"
            ]
        }
    ) as server:
        agent = Agent(
            "Assistant",
            instructions="You are a helpful assistant",
            model="gpt-4.1",
            mcp_servers=[server],
        )
        runner = await Runner.run(agent, input="Open Puppeteer, go to abidportfolio-web.vercel.app")
        print(runner.final_output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

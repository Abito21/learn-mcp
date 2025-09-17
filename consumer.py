from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()


def main():
    agent = Agent(
        "Assistant", instruction="You are a helpful assistant", model="gpt-4.1"
    )
    runner = Runner.run_sync(agent, input="Hello!")
    print(runner.final_output)

if __name__ == "__main__":
    main()

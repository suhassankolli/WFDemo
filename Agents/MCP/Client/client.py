from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools

from langgraph.prebuilt import create_react_agent

from langchain_groq import ChatGroq

from dotenv import load_dotenv
import asyncio

load_dotenv()

model = ChatGroq(model="qwen-2.5-32b")

server_params= StdioServerParameters(
    command=r"D:\learning\Gen AI\WFDemo\venvWFDemo\python.exe",
    args=["Agents\MCP\server\math_server.py"]
)
async def main(input):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            ## Get tools
            tools = await load_mcp_tools(session=session)

            ## Create and run the agent
            agent = create_react_agent(model, tools)
            response = await agent.ainvoke({"messages":input })
            return response

if __name__ == "__main__":
    input="what is (3+5) * (10+1)"
    result = asyncio.run(main(input))
    print(result['messages'][-1].content)
from typing import Annotated
from typing_extensions import TypedDict

import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


# Load environment variables
load_dotenv()


# LLM
llm = init_chat_model(
    "groq:openai/gpt-oss-20b"
)


# State
class State(TypedDict):
    messages: Annotated[
        list[BaseMessage],
        add_messages
    ]


def make_tool_graph():

    # Tool
    @tool
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    tools = [add]

    # Bind tools to LLM
    llm_with_tools = llm.bind_tools(tools)

    # LLM node
    def call_llm_model(state: State):
        response = llm_with_tools.invoke(
            state["messages"]
        )

        return {
            "messages": [response]
        }

    # Create graph
    builder = StateGraph(State)

    # Nodes
    builder.add_node(
        "tool_calling_llm",
        call_llm_model
    )

    builder.add_node(
        "tools",
        ToolNode(tools)
    )

    # START → LLM
    builder.add_edge(
        START,
        "tool_calling_llm"
    )

    # LLM → tools OR END
    builder.add_conditional_edges(
        "tool_calling_llm",
        tools_condition
    )

    # Tools → LLM
    builder.add_edge(
        "tools",
        "tool_calling_llm"
    )

    # Compile
    graph = builder.compile()

    return graph


# IMPORTANT:
# langgraph.json points to ./agent.py:agent
agent = make_tool_graph()
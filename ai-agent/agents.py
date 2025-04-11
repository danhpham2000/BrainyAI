from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st
from typing_extensions import TypedDict
from typing import Annotated


@tool
def generate_summary():
    """
    This tool use for generate summart based on given document: PDF file
    """
    pass

@tool
def generate_quiz():
    """
    This tool use for generating quiz for user to test the learning performance also based on
    document and given subject as well
    """
    pass

@tool
def generate_exam():
    """
    This tool use for generate practice exam for user to prepare for exam based on given subject
    """
    pass


memory = MemorySaver()

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)


model = ChatOpenAI(api_key=st.secrets["OPENAI_API_KEY"])
tools = [generate_summary, generate_quiz, generate_exam]

model_with_tools = model.bind_tools(tools)


def chatbot(state: State):
    return {"messages": [model_with_tools.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
tool_node = ToolNode(tools=[generate_summary, generate_quiz, generate_exam])
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges("chatbot", tools_condition)

graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")


graph = graph_builder.compile(checkpointer=memory)














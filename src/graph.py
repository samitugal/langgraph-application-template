import os
from dotenv import load_dotenv
from langgraph.graph import END, StateGraph

from src.const import *
from src.Nodes import *
from src.state_model import GraphState

load_dotenv()


workflow = StateGraph(GraphState)

"""
    Langgraph Graph definition for the application.
    You must implement the nodes in src/Nodes.py
    You can add new nodes to the graph by adding them to the graph variable.
    You can also add decorators to the nodes by adding them to the node variable.
"""

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph-schema.png")

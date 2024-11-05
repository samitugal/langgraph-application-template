from src.graph import app
from langfuse.utils.langfuse_singleton import LangfuseSingleton # type: ignore
from src.LLM.config_defs import LLMMainConfig
from src.LLM.Pipeline import Pipeline
from src.output_models import ExampleOutput
"""
    Method definitions for the main application.
    You should define your methods here to use in server.py
"""

def example_method(content: str) -> ExampleOutput:
    pass
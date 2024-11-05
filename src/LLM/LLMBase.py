import os
import string
from typing import Any, Dict, List, TypeVar

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from ..output_models import *
from .LLMAbstractBase import LLMAbstractBase

U = TypeVar("U", bound=BaseModel)

class LLMBase(LLMAbstractBase):
    def __init__(self, config):
        self.config = config
        load_dotenv()

    def example_method(self, content: str) -> ExampleOutput:
        """
        This function is an example for invoking the LLM.
        You should initialize your prompt and output parser here.
        Finally invoke the llm with content as the input.
        """

        output_parser = PydanticOutputParser(pydantic_object=ExampleOutput)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "prompt for system directive"),
            ("human", f"{content}"),
            ("human", "Format the output as follows:\n{format_instructions}")
        ]).partial(format_instructions=output_parser.get_format_instructions())
        
        chain = prompt | self.client | output_parser

        response = chain.invoke({"content": content})
        return response
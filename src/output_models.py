from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class ExampleOutput(BaseModel):
    example_field: str = Field(description="This is an example field")

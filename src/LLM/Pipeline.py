from typing import Any, Dict, List

from ..output_models import *
from .config_defs import LLMTag
from .LLMBase import LLMBase


class Pipeline:
    def __init__(self, config, llm: LLMBase):
        self.config = config
        self.llm = llm

    @staticmethod
    def new_instance_from_config(config) -> "Pipeline":
        from .example_llm_model import ExampleLLM

        match config.llm.llm_tag:
            case LLMTag.EXAMPLE:
                return Pipeline(config, ExampleLLM(config))
            case _:
                raise ValueError("Invalid LLM tag")

    def example_method(self):
        pass

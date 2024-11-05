import warnings

from langchain_openai import ChatOpenAI

from .config_defs import LLMMainConfig, LLMTag
from .LLMBase import LLMBase

warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")


class ExampleLLM(LLMBase):
    def __init__(self, config):
        """
            Example LLM class for the application template.
            You can initialize Bedrock or OpenAI LLM here.
            Just initialize your ChatOpenAI or Bedrock here and assign to self.client.
        """
        super().__init__(config)
        
        self.client = None
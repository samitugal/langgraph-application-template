from abc import ABC, abstractmethod

from ..output_models import *


class LLMAbstractBase(ABC):

    @abstractmethod
    def example_method(self, content: str) -> ExampleOutput:
        pass

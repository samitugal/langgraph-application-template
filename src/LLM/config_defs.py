from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

import omegaconf
from omegaconf import OmegaConf

"""
    Configs definition class for the LLM.
    These classes must match with config.yaml file.
"""

class LLMTag(Enum):
    EXAMPLE = "example"
    EXAMPLE2 = "example2"



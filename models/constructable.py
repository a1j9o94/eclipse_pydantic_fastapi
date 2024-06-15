from pydantic import BaseModel, Field
from typing import List, Optional, Dict
import random
import uuid
from enum import Enum
from .blueprint import Blueprint
from .enums import ConstructableType

class Constructable(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: ConstructableType
    blueprint: Optional[Blueprint]
    material_cost: int


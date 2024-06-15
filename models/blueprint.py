from pydantic import BaseModel, Field
import uuid
from typing import List, Optional, Dict
import random
from .part import Part

class Blueprint(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    parts: List[Part]
    capacity: int


from pydantic import BaseModel, Field
import uuid
from typing import List, Optional, Dict
import random

class DiceFace(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    damage: int
    text: str

class Dice(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    diceFaces: List[DiceFace]


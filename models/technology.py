from pydantic import BaseModel, Field
from enum import Enum
import uuid
from typing import List, Optional, Dict, Callable
from .faction import Faction
from .part import Part
from .enums import TechType


class Technology(BaseModel):
    '''
        Techs in eclipse have a type (1 of 4 military, grid, nano, and rare), a normal cost, and a minimum cost

        They either have an associated part, or some kind of effect that applies to the player
    '''
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    part: Optional[Part] = None
    minimum_cost:int = None
    maximum_cost:int = None
    type: TechType
    effect: Optional[str] = None


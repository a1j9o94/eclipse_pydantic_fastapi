from pydantic import BaseModel
from typing import List, Optional, Dict
import random
import uuid
from pydantic import Field
from .dice import Dice, DiceFace

class Part(BaseModel):
    # create an Id as a UUID
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str
    energyCost: int
    name: str
    triggerEffect: Optional[str] = None  # assuming triggerEffect as string for simplicity

class Hull(Part):
    hullPoints: int

class Cannon(Part):
    dice: List[Dice]
    
    def roll_dice(self) -> List[DiceFace]:
        return [die.diceFaces[random.randint(0, len(die.diceFaces) - 1)] for die in self.dice]

class Missile(Part):
    dice: List[Dice]

    def roll_dice(self) -> List[DiceFace]:
        return [die.diceFaces[random.randint(0, len(die.diceFaces) - 1)] for die in self.dice]

class Shield(Part):
    shieldPoints: int

class Energy(Part):
    energyPoints: int

class Computer(Part):
    rollBonus: int

class Drive(Part):
    move: int
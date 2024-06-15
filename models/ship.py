from pydantic import BaseModel
from .blueprint import Blueprint

class Ship(BaseModel):
    materialCosts: int
    blueprint: Blueprint
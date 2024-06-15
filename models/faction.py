from pydantic import BaseModel, Field
from typing import List, Dict
import uuid
from .sector_tile import SectorTile
from .blueprint import Blueprint
from .enums import ConstructableType, ActionType, FactionList

class Faction(BaseModel):
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    max_influence_disks: int
    # must be the same length as the number of influence disks the faction has
    influence_costs: List[int]
    reputation_capacity: int
    ambassador_capacity: int
    colony_ships: List[bool]
    default_blueprints: Dict[ConstructableType, Blueprint] = {
        ConstructableType.interceptor: None,
        ConstructableType.cruiser: None,
        ConstructableType.dreadnought: None,
        ConstructableType.starbase: None,
    }
    '''
        Has to have Explore, Build, Research, Move, Upgrade, Influence
    '''
    actions: Dict[ActionType, int] = {
        ActionType.Explore: 0, ActionType.Build: 0, ActionType.Research: 0, ActionType.Move: 0, ActionType.Upgrade: 0, ActionType.Influence: 0
    }
    starting_sector: SectorTile
    trade_ratio: int
    setup_faction: FactionList
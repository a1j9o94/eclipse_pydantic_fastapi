from pydantic import BaseModel
from typing import List, Optional, Dict
import random

class DiceFace(BaseModel):
    damage: int

class Dice(BaseModel):
    diceFaces: List[DiceFace]

class Part(BaseModel):
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

class Blueprint(BaseModel):
    parts: List[Part]
    capacity: int

class Constructable(BaseModel):
    materialCosts: int

class DiceFace(BaseModel):
    damage: int

class Dice(BaseModel):
    diceFaces: List[DiceFace]

class DiscoveryTile(BaseModel):
    benefit: Optional[Part]
    reveal: bool = False
    collectable: bool = False
    points: int = 0
    collect: Optional[str] = None  # assuming collect as string for simplicity

class NPC(BaseModel):
    name: str
    blueprint: Blueprint
    damage: int

class Planet(BaseModel):
    resource: str
    populated: bool = False

class ReputationTile(BaseModel):
    points: int

class TileEdge(BaseModel):
    hasWormhole: bool
    connectedTile: Optional[int] = None

class Ship(BaseModel):
    materialCosts: int
    blueprint: Blueprint

class Faction(BaseModel):
    id: int
    name: str
    max_influence_disks: int
    influence_costs: List[int]
    reputation_capacity: int
    ambassador_capacity: int
    colony_ships: List[bool]
    default_blueprints: List[Blueprint]
    '''
        Has to have Explore, Build, Research, Move, Upgrade, Influence
    '''
    actions: Dict[str, int] = {
        "Explore": 0, "Build": 0, "Research": 0, "Move": 0, "Upgrade": 0, "Influence": 0
    }
    starting_sector: SectorTile
    trade_ratio: int

class Player(BaseModel):
    faction: Faction
    color: str
    discoveryTiles: List[DiscoveryTile] = []
    reputationTiles: List[dict] = []  # simplified for now
    resource_tracks: Dict[str, List[int]] = {
        "gold": [0, 1, 2, 3, 4, 5],
        "science": [0, 1, 2, 3, 4, 5],
        "materials": [0, 1, 2, 3, 4, 5]
    }
    resource_cubes_placed: Dict[str, int] = {
        "gold": 0,
        "science": 0,
        "materials": 0
    }
    choice: int = -1

    def update_resources(self):
        for resource_type in ["gold", "science", "materials"]:
            if self.resource_cubes_placed[resource_type] < len(self.resource_tracks[resource_type]):
                self.resources[resource_type] = self.resource_tracks[resource_type][self.resource_cubes_placed[resource_type]]
            else:
                self.resources[resource_type] = self.resource_tracks[resource_type][-1]



class SectorTile(BaseModel):
    id: int
    edges: List[TileEdge]
    planets: List[Planet]
    npcs: Optional[List[NPC]] = None
    discoveryTile: Optional[DiscoveryTile] = None
    point_value: int
    artifact: bool
    owner: Optional[Player] = None
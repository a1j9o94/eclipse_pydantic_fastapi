from enum import Enum

class ResourceType(Enum):
    Gold = 0
    Science = 1
    Materials = 2


class ConstructableType(str, Enum):
    interceptor = "interceptor"
    cruiser = "cruiser"
    dreadnought = "dreadnought"
    starbase = "starbase"
    monolith = "monolith"
    orbital = "orbital"

class ActionType(Enum):
    Explore = 0
    Build = 1
    Research = 2
    Move = 3
    Upgrade = 4
    Influence = 5

class TechType(Enum):
    military = 1
    grid = 2
    nano = 3
    rare = 4

class GamePhase(Enum):
    Action = "Action"
    Combat = "Combat"
    Upkeep = "Upkeep"
    Cleanup = "Cleanup"

class SectorRing(Enum):
    center = 1
    ring1 = 2
    ring2 = 3
    ring3 = 4

class FactionList(Enum):
    Terran = 1

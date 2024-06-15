from pydantic import BaseModel, Field
from typing import List, Optional, Dict
import random
import uuid
from .part import Part
from .blueprint import Blueprint
from .enums import ResourceType, SectorRing

class DiscoveryTile(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    benefit: Optional[Part]
    reveal: bool = False
    collectable: bool = False
    points: int = 0
    collect: Optional[str] = None  # assuming collect as string for simplicity

class NPC(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    blueprint: Blueprint
    damage: int

class Planet(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    resource: ResourceType
    is_advanced: bool = False
    is_populated: bool = False

class TileEdge(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    hasWormhole: bool
    connectedTile: Optional[int] = None

class SectorTile(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    ring: SectorRing
    edges: List[TileEdge]
    planets: List[Planet]
    npcs: Optional[List[NPC]] = None
    discoveryTile: Optional[DiscoveryTile] = None
    point_value: int
    artifact: bool
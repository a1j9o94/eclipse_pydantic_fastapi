'''
    A class that represents the total current game state and a class that represents a single action taken

    You should be able to trace the history of actions taken by creating a list of Action objects that will create any given game state object

    I want to structure it as a linked list of game actions where each one has a prior and a next action, and an associated game state
'''

from pydantic import BaseModel, List, Field
from uuid import UUID
from models.player import Player
from models.sector_tile import SectorTile, DiscoveryTile
from models.enums import GamePhase
from models.technology import Technology

class GameState(BaseModel):
    id: UUID = Field(default_factory=UUID)
    players: List[Player]
    # 8 rounds of game play, winner is determined at the end of the 8th round
    round: int
    # Each round is divided in to 4 phases, Action, Combat, Upkeep, Cleanup
    phase: GamePhase
    #The player currently acting
    current_player: Player
    # board of sector tiles
    board: List[SectorTile]
    tile_bag: List[SectorTile]
    tech_tray: List[Technology]
    discovery_tiles: List[DiscoveryTile]
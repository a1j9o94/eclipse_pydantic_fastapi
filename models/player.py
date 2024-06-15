from pydantic import BaseModel, Field
from typing import List, Dict
import uuid
from enum import Enum
from .faction import Faction
from .sector_tile import DiscoveryTile, SectorTile
from .technology import Technology
from .enums import ResourceType, TechType

class Player(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    faction: Faction
    color: str
    discoveryTiles: List[DiscoveryTile] = []
    reputationTiles: List[dict] = []  # simplified for now
    owned_sectors: List[SectorTile] = []
    resource_tracks: Dict[ResourceType, List[int]] = {
        ResourceType.Gold: [0, 1, 2, 3, 4, 5],
        ResourceType.Science: [0, 1, 2, 3, 4, 5],
        ResourceType.Materials: [0, 1, 2, 3, 4, 5]
    }
    resource_cubes_placed: Dict[ResourceType, int] = {
        ResourceType.Gold: 0,
        ResourceType.Science: 0,
        ResourceType.Materials: 0
    }

    # the total pool of resources available to the player
    resources: Dict[ResourceType, int] = {
        ResourceType.Gold: 0,
        ResourceType.Science: 0,
        ResourceType.Materials: 0
    }

    # Indicates which sets of advanced techs the player has access to
    advanced_resources: List[ResourceType] = []

    # there are 3 tech tracks, rare can be played in any of the 3 tracks.
    tech_tracks: Dict[TechType, Dict[int, Technology]] = {
        TechType.military: {0: None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 8:None},
        TechType.grid: {0: None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 8:None},
        TechType.nano: {0: None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 8:None},
    }
    choice: int = -1

    # Increase the amount of resources available to each player. Should run at the end of each round
    def gather_resources(self):
        for resource_type in ResourceType:
            #Check if we have more spaces to take cubes off of
            if self.resource_cubes_placed[resource_type] < len(self.resource_tracks[resource_type]):
                self.resources[resource_type] += self.resource_tracks[resource_type][self.resource_cubes_placed[resource_type]]
            else:
                self.resources[resource_type] = self.resource_tracks[resource_type][-1]
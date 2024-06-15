from pydantic import BaseModel
from typing import Optional, Callable, List
from database import players_db, factions_db
from models.player import Player
from models.faction import Faction
from models.technology import Technology
from models.blueprint import Blueprint
from models.sector_tile import SectorTile
from models.enums import ResourceType, SectorRing
import random
from game_state import GameState
from logger import logging

class GameAction(BaseModel):
    impacted_objects: List[str]
    action: Optional[Callable[..., GameState]]
    description: str
    prior_action: Optional['GameAction'] = None


class SetUpGame(GameAction):
    def action(self, game_state: GameState, players: List[Player], technologies: List[Technology], factions: List[Faction], sector_bag: List[SectorTile], ancient_blueprint: Blueprint, guardian_blueprint: Blueprint, gcds_blueprint: Blueprint) -> GameState:
        # Initialize the game state with the provided players, technologies, and factions
        game_state.players = players
        game_state.technology_bag = technologies
        game_state.faction_options = factions

        # Set up sector tiles
        outer_sector_counts = {2: 5, 3: 8, 4: 14, 5: 16, 6: 18}
        num_outer_sectors = outer_sector_counts[len(players)]
        #grab all of the center, ring 1, and ring 2 tiles
        game_state.sector_tiles.append(next((tile for tile in sector_bag if tile.ring == SectorRing.center), None))
        game_state.sector_tiles.append(next((tile for tile in sector_bag if tile.ring == SectorRing.ring1), None))
        game_state.sector_tiles.append(next((tile for tile in sector_bag if tile.ring == SectorRing.ring2), None))
        tier3_tiles = [tile for tile in sector_bag if tile.ring == SectorRing.ring3]
        random_tier3_sample = random.sample(tier3_tiles, num_outer_sectors)
        game_state.sector_tiles.append(random_tier3_sample)

        game_state.ancient_blueprint = ancient_blueprint
        game_state.guardian_blueprint = guardian_blueprint
        game_state.gcds_blueprint = gcds_blueprint

        return game_state

class SelectFaction(GameAction):
    
    def action(self, game_state: GameState, player_id: str, faction_id: str):

        player = next((p for p in game_state.players if p.id == player_id), None)
        faction = next((f for f in factions_db if f.id == faction_id), None)
        
        if player and faction:
            player.faction = faction
            player.faction.setup_faction()
            # add the faction starting sector tile to the game states list of sector tiles
            game_state.sector_tiles.append(faction.starting_sector_tile)

            #go through the list of planets in the starting sector tile, based on the type of resource, increment the players resource count for that type
            for planet in faction.starting_sector_tile.planets:
                if not planet.is_advanced:
                    player.resource_cubes_placed[planet.resource] += 1
                    planet.is_populated = True
                elif planet.resource in player.advanced_resources:
                    player.resource_cubes_placed[planet.resource] += 1
                    planet.is_populated = True
                else:
                    logging.info("Attempted to populate an advanced planet without the required tech")
                    planet.is_populated = False
            return game_state
        return None
    
class BeginRound(GameAction):
    def action(self, game_state: GameState):
        # Set up tech tiles based on player count
        tech_tile_counts = {2: 12, 3: 14, 4: 16, 5: 18, 6: 20}
        num_tech_tiles = tech_tile_counts[len(game_state.players)]
        #add a new set of techs to the tech tray that havent been used yet in the tech_bag based on the number of players
        game_state.tech_tray = game_state.tech_tray + random.sample(game_state.technology_bag, num_tech_tiles)
        game_state.round += 1
        return game_state

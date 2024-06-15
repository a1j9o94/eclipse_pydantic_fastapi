from models.part import Part
from models.blueprint import Blueprint
from models.sector_tile import DiscoveryTile, SectorTile, TileEdge, NPC, Planet
from models.faction import Faction, ActionType
from models.player import Player
from models.reputation_tile import ReputationTile
from models.ship import Ship
from models.technology import Technology
from models.dice import Dice, DiceFace
from models.constructable import Constructable
from models.enums import ResourceType, TechType, ConstructableType, SectorRing, FactionList

# In-memory data store
# In-memory data store with dummy data
parts_db = [
    Part(type="cannon", energyCost=2, name="Laser Cannon"),
    Part(type="shield", energyCost=3, name="Deflector Shield"),
]

blueprints_db = [
    Blueprint(parts=[parts_db[0]], capacity=5)
]

discovery_tiles_db = [
    DiscoveryTile(benefit=parts_db[0], points=2, collect="Increase attack power"),
    DiscoveryTile(benefit=None, points=1, collect="Gain 3 resources")
]

planets_db = [
    Planet(resource=ResourceType.Gold),
    Planet(resource=ResourceType.Science)
]

reputation_tiles_db = [
    ReputationTile(points=2),
    ReputationTile(points=3)
]

tile_edges_db = [
    TileEdge(hasWormhole=True),
    TileEdge(hasWormhole=False)
]

sector_tiles_db = [
    SectorTile(
        ring=SectorRing.ring1,
        edges=[tile_edges_db[0], tile_edges_db[1], tile_edges_db[0], tile_edges_db[1], tile_edges_db[0], tile_edges_db[1]],
        planets=planets_db,
        npcs=[],
        discoveryTile=discovery_tiles_db[0],
        point_value=2,
        artifact=False
    )
]

ships_db = [
    Ship(materialCosts=10, blueprint=blueprints_db[0])
]

npcs_db = [
    NPC(name="Acient", damage=0, blueprint=blueprints_db[0])
]

technologies_db = [
    Technology(type=TechType.military, minimum_cost=1, maximum_cost=3, effect=None)
]

constructables_db = [
    Constructable(type=ConstructableType.monolith, material_cost=10, blueprint=None)
]

factions_db = [
    Faction(
        name="Terran",
        max_influence_disks=3,
        influence_costs=[1, 2, 3],
        reputation_capacity=4,
        ambassador_capacity=2,
        colony_ships=[True, True, True],
        default_blueprints={
            ConstructableType.interceptor: Blueprint(parts=[parts_db[0]], capacity=5),
            ConstructableType.cruiser: Blueprint(parts=[parts_db[0], parts_db[1]], capacity=5),
            ConstructableType.dreadnought: Blueprint(parts=[parts_db[0], parts_db[1]], capacity=5),
            ConstructableType.starbase: Blueprint(parts=[parts_db[0], parts_db[1]], capacity=5)
        },
        actions={ActionType.Explore: 1, ActionType.Build: 1, ActionType.Research: 1, ActionType.Move: 1, ActionType.Upgrade: 1, ActionType.Influence: 1},
        starting_sector=sector_tiles_db[0],
        trade_ratio=2,
        # function that takes in a string of a player id and runs a function
        setup_faction = FactionList.Terran
    )
]

def setup_faction(faction_id: str, player_id: str):
    current_player = None
    current_faction = None
    # find the player
    for player in players_db:
        if player.id == player_id:
            current_player = player 
            break

    # find the faction
    for faction in factions_db:
        if faction.id == faction_id:
            current_faction = faction
            break
    
    current_player.faction = current_faction
    
    # get the starting sector tile from the faction
    starting_sector = current_faction.starting_sector
    
    # add the starting sector to the player's sectors
    current_player.owned_sectors.append(starting_sector)

    #loop through all of the planets in this sector and place a resource cube based on the resource type of the planet
    for planet in starting_sector.planets:
        current_player.resource_cubes_placed[planet.resource] += 1

    # gather the first set of resources for the player
    current_player.gather_resources()

    # reduce the reputation capacity to show the reputation disk that was used
    current_faction.reputation_capacity -= 1
    pass

faction_setup_functions_db = {
    FactionList.Terran: setup_faction
}

players_db = [
    Player(
        faction=factions_db[0],
        color="red"
    )
]

dice_db = [
    Dice(diceFaces=[DiceFace(damage=1, text="1"), DiceFace(damage=2, text="2"), DiceFace(damage=3, text="3")])
]
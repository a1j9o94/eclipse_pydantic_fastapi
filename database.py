from models import (
    Part, Blueprint, DiscoveryTile, Faction, 
    Planet, Player, ReputationTile, TileEdge, SectorTile, Ship, NPC
)

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

factions_db = [
    Faction(
        id=1,
        name="Terran",
        max_influence_disks=5,
        influence_costs=[1, 2, 3],
        reputation_capacity=4,
        ambassador_capacity=2,
        colony_ships=[True, True, True],
        default_blueprints=blueprints_db,
        actions={"Explore": 1, "Build": 1, "Research": 1, "Move": 1, "Upgrade": 1, "Influence": 1},
        starting_resources=[{"gold": 3}, {"science": 2}, {"materials": 2}],
        trade_ratio=2
    )
]

planets_db = [
    Planet(resource="gold"),
    Planet(resource="science")
]

players_db = [
    Player(
        faction=factions_db[0],
        color="red"
    )
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
        id=1,
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


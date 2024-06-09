# main.py

from fastapi import FastAPI, HTTPException
from typing import List
from models import (
    Part, Blueprint, DiscoveryTile, Faction, 
    NPC, Planet, Player, ReputationTile, TileEdge, SectorTile, Ship
)
from database import (
    parts_db, blueprints_db, discovery_tiles_db, factions_db, npcs_db, planets_db, players_db, reputation_tiles_db, tile_edges_db, sector_tiles_db, ships_db
)

app = FastAPI()

# Part Endpoints
@app.post("/parts/", response_model=Part)
def create_part(part: Part):
    parts_db.append(part)
    return part

@app.get("/parts/", response_model=List[Part])
def read_parts():
    return parts_db

@app.get("/parts/{part_id}", response_model=Part)
def read_part(part_id: int):
    if part_id >= len(parts_db):
        raise HTTPException(status_code=404, detail="Part not found")
    return parts_db[part_id]

@app.put("/parts/{part_id}", response_model=Part)
def update_part(part_id: int, part: Part):
    if part_id >= len(parts_db):
        raise HTTPException(status_code=404, detail="Part not found")
    parts_db[part_id] = part
    return part

@app.delete("/parts/{part_id}", response_model=Part)
def delete_part(part_id: int):
    if part_id >= len(parts_db):
        raise HTTPException(status_code=404, detail="Part not found")
    part = parts_db.pop(part_id)
    return part

# Blueprint Endpoints
@app.post("/blueprints/", response_model=Blueprint)
def create_blueprint(blueprint: Blueprint):
    blueprints_db.append(blueprint)
    return blueprint

@app.get("/blueprints/", response_model=List[Blueprint])
def read_blueprints():
    return blueprints_db

@app.get("/blueprints/{blueprint_id}", response_model=Blueprint)
def read_blueprint(blueprint_id: int):
    if blueprint_id >= len(blueprints_db):
        raise HTTPException(status_code=404, detail="Blueprint not found")
    return blueprints_db[blueprint_id]

@app.put("/blueprints/{blueprint_id}", response_model=Blueprint)
def update_blueprint(blueprint_id: int, blueprint: Blueprint):
    if blueprint_id >= len(blueprints_db):
        raise HTTPException(status_code=404, detail="Blueprint not found")
    blueprints_db[blueprint_id] = blueprint
    return blueprint

@app.delete("/blueprints/{blueprint_id}", response_model=Blueprint)
def delete_blueprint(blueprint_id: int):
    if blueprint_id >= len(blueprints_db):
        raise HTTPException(status_code=404, detail="Blueprint not found")
    blueprint = blueprints_db.pop(blueprint_id)
    return blueprint

# DiscoveryTile Endpoints
@app.post("/discovery_tiles/", response_model=DiscoveryTile)
def create_discovery_tile(discovery_tile: DiscoveryTile):
    discovery_tiles_db.append(discovery_tile)
    return discovery_tile

@app.get("/discovery_tiles/", response_model=List[DiscoveryTile])
def read_discovery_tiles():
    return discovery_tiles_db

@app.get("/discovery_tiles/{discovery_tile_id}", response_model=DiscoveryTile)
def read_discovery_tile(discovery_tile_id: int):
    if discovery_tile_id >= len(discovery_tiles_db):
        raise HTTPException(status_code=404, detail="DiscoveryTile not found")
    return discovery_tiles_db[discovery_tile_id]

@app.put("/discovery_tiles/{discovery_tile_id}", response_model=DiscoveryTile)
def update_discovery_tile(discovery_tile_id: int, discovery_tile: DiscoveryTile):
    if discovery_tile_id >= len(discovery_tiles_db):
        raise HTTPException(status_code=404, detail="DiscoveryTile not found")
    discovery_tiles_db[discovery_tile_id] = discovery_tile
    return discovery_tile

@app.delete("/discovery_tiles/{discovery_tile_id}", response_model=DiscoveryTile)
def delete_discovery_tile(discovery_tile_id: int):
    if discovery_tile_id >= len(discovery_tiles_db):
        raise HTTPException(status_code=404, detail="DiscoveryTile not found")
    discovery_tile = discovery_tiles_db.pop(discovery_tile_id)
    return discovery_tile

# Faction Endpoints
@app.post("/factions/", response_model=Faction)
def create_faction(faction: Faction):
    factions_db.append(faction)
    return faction

@app.get("/factions/", response_model=List[Faction])
def read_factions():
    return factions_db

@app.get("/factions/{faction_id}", response_model=Faction)
def read_faction(faction_id: int):
    if faction_id >= len(factions_db):
        raise HTTPException(status_code=404, detail="Faction not found")
    return factions_db[faction_id]

@app.put("/factions/{faction_id}", response_model=Faction)
def update_faction(faction_id: int, faction: Faction):
    if faction_id >= len(factions_db):
        raise HTTPException(status_code=404, detail="Faction not found")
    factions_db[faction_id] = faction
    return faction

@app.delete("/factions/{faction_id}", response_model=Faction)
def delete_faction(faction_id: int):
    if faction_id >= len(factions_db):
        raise HTTPException(status_code=404, detail="Faction not found")
    faction = factions_db.pop(faction_id)
    return faction

# NPC Endpoints
@app.post("/npcs/", response_model=NPC)
def create_npc(npc: NPC):
    npcs_db.append(npc)
    return npc

@app.get("/npcs/", response_model=List[NPC])
def read_npcs():
    return npcs_db

@app.get("/npcs/{npc_id}", response_model=NPC)
def read_npc(npc_id: int):
    if npc_id >= len(npcs_db):
        raise HTTPException(status_code=404, detail="NPC not found")
    return npcs_db[npc_id]

@app.put("/npcs/{npc_id}", response_model=NPC)
def update_npc(npc_id: int, npc: NPC):
    if npc_id >= len(npcs_db):
        raise HTTPException(status_code=404, detail="NPC not found")
    npcs_db[npc_id] = npc
    return npc

@app.delete("/npcs/{npc_id}", response_model=NPC)
def delete_npc(npc_id: int):
    if npc_id >= len(npcs_db):
        raise HTTPException(status_code=404, detail="NPC not found")
    npc = npcs_db.pop(npc_id)
    return npc

# Planet Endpoints
@app.post("/planets/", response_model=Planet)
def create_planet(planet: Planet):
    planets_db.append(planet)
    return planet

@app.get("/planets/", response_model=List[Planet])
def read_planets():
    return planets_db

@app.get("/planets/{planet_id}", response_model=Planet)
def read_planet(planet_id: int):
    if planet_id >= len(planets_db):
        raise HTTPException(status_code=404, detail="Planet not found")
    return planets_db[planet_id]

@app.put("/planets/{planet_id}", response_model=Planet)
def update_planet(planet_id: int, planet: Planet):
    if planet_id >= len(planets_db):
        raise HTTPException(status_code=404, detail="Planet not found")
    planets_db[planet_id] = planet
    return planet

@app.delete("/planets/{planet_id}", response_model=Planet)
def delete_planet(planet_id: int):
    if planet_id >= len(planets_db):
        raise HTTPException(status_code=404, detail="Planet not found")
    planet = planets_db.pop(planet_id)
    return planet

# Player Endpoints
@app.post("/players/", response_model=Player)
def create_player(player: Player):
    players_db.append(player)
    return player

@app.get("/players/", response_model=List[Player])
def read_players():
    return players_db

@app.get("/players/{player_id}", response_model=Player)
def read_player(player_id: int):
    if player_id >= len(players_db):
        raise HTTPException(status_code=404, detail="Player not found")
    return players_db[player_id]

@app.put("/players/{player_id}", response_model=Player)
def update_player(player_id: int, player: Player):
    if player_id >= len(players_db):
        raise HTTPException(status_code=404, detail="Player not found")
    players_db[player_id] = player
    return player

@app.delete("/players/{player_id}", response_model=Player)
def delete_player(player_id: int):
    if player_id >= len(players_db):
        raise HTTPException(status_code=404, detail="Player not found")
    player = players_db.pop(player_id)
    return player

# ReputationTile Endpoints
@app.post("/reputation_tiles/", response_model=ReputationTile)
def create_reputation_tile(reputation_tile: ReputationTile):
    reputation_tiles_db.append(reputation_tile)
    return reputation_tile

@app.get("/reputation_tiles/", response_model=List[ReputationTile])
def read_reputation_tiles():
    return reputation_tiles_db

@app.get("/reputation_tiles/{reputation_tile_id}", response_model=ReputationTile)
def read_reputation_tile(reputation_tile_id: int):
    if reputation_tile_id >= len(reputation_tiles_db):
        raise HTTPException(status_code=404, detail="ReputationTile not found")
    return reputation_tiles_db[reputation_tile_id]

@app.put("/reputation_tiles/{reputation_tile_id}", response_model=ReputationTile)
def update_reputation_tile(reputation_tile_id: int, reputation_tile: ReputationTile):
    if reputation_tile_id >= len(reputation_tiles_db):
        raise HTTPException(status_code=404, detail="ReputationTile not found")
    reputation_tiles_db[reputation_tile_id] = reputation_tile
    return reputation_tile

@app.delete("/reputation_tiles/{reputation_tile_id}", response_model=ReputationTile)
def delete_reputation_tile(reputation_tile_id: int):
    if reputation_tile_id >= len(reputation_tiles_db):
        raise HTTPException(status_code=404, detail="ReputationTile not found")
    reputation_tile = reputation_tiles_db.pop(reputation_tile_id)
    return reputation_tile

# TileEdge Endpoints
@app.post("/tile_edges/", response_model=TileEdge)
def create_tile_edge(tile_edge: TileEdge):
    tile_edges_db.append(tile_edge)
    return tile_edge

@app.get("/tile_edges/", response_model=List[TileEdge])
def read_tile_edges():
    return tile_edges_db

@app.get("/tile_edges/{tile_edge_id}", response_model=TileEdge)
def read_tile_edge(tile_edge_id: int):
    if tile_edge_id >= len(tile_edges_db):
        raise HTTPException(status_code=404, detail="TileEdge not found")
    return tile_edges_db[tile_edge_id]

@app.put("/tile_edges/{tile_edge_id}", response_model=TileEdge)
def update_tile_edge(tile_edge_id: int, tile_edge: TileEdge):
    if tile_edge_id >= len(tile_edges_db):
        raise HTTPException(status_code=404, detail="TileEdge not found")
    tile_edges_db[tile_edge_id] = tile_edge
    return tile_edge

@app.delete("/tile_edges/{tile_edge_id}", response_model=TileEdge)
def delete_tile_edge(tile_edge_id: int):
    if tile_edge_id >= len(tile_edges_db):
        raise HTTPException(status_code=404, detail="TileEdge not found")
    tile_edge = tile_edges_db.pop(tile_edge_id)
    return tile_edge

# SectorTile Endpoints
@app.post("/sector_tiles/", response_model=SectorTile)
def create_sector_tile(sector_tile: SectorTile):
    sector_tiles_db.append(sector_tile)
    return sector_tile

@app.get("/sector_tiles/", response_model=List[SectorTile])
def read_sector_tiles():
    return sector_tiles_db

@app.get("/sector_tiles/{sector_tile_id}", response_model=SectorTile)
def read_sector_tile(sector_tile_id: int):
    if sector_tile_id >= len(sector_tiles_db):
        raise HTTPException(status_code=404, detail="SectorTile not found")
    return sector_tiles_db[sector_tile_id]

@app.put("/sector_tiles/{sector_tile_id}", response_model=SectorTile)
def update_sector_tile(sector_tile_id: int, sector_tile: SectorTile):
    if sector_tile_id >= len(sector_tiles_db):
        raise HTTPException(status_code=404, detail="SectorTile not found")
    sector_tiles_db[sector_tile_id] = sector_tile
    return sector_tile

@app.delete("/sector_tiles/{sector_tile_id}", response_model=SectorTile)
def delete_sector_tile(sector_tile_id: int):
    if sector_tile_id >= len(sector_tiles_db):
        raise HTTPException(status_code=404, detail="SectorTile not found")
    sector_tile = sector_tiles_db.pop(sector_tile_id)
    return sector_tile

# Ship Endpoints
@app.post("/ships/", response_model=Ship)
def create_ship(ship: Ship):
    ships_db.append(ship)
    return ship

@app.get("/ships/", response_model=List[Ship])
def read_ships():
    return ships_db

@app.get("/ships/{ship_id}", response_model=Ship)
def read_ship(ship_id: int):
    if ship_id >= len(ships_db):
        raise HTTPException(status_code=404, detail="Ship not found")
    return ships_db[ship_id]

@app.put("/ships/{ship_id}", response_model=Ship)
def update_ship(ship_id: int, ship: Ship):
    if ship_id >= len(ships_db):
        raise HTTPException(status_code=404, detail="Ship not found")
    ships_db[ship_id] = ship
    return ship

@app.delete("/ships/{ship_id}", response_model=Ship)
def delete_ship(ship_id: int):
    if ship_id >= len(ships_db):
        raise HTTPException(status_code=404, detail="Ship not found")
    ship = ships_db.pop(ship_id)
    return ship
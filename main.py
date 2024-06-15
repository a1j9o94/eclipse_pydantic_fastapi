# main.py

from fastapi import FastAPI, HTTPException
from typing import List
from models.part import Part
from models.blueprint import Blueprint
from models.sector_tile import SectorTile
from models.faction import Faction
from models.player import Player
from models.reputation_tile import ReputationTile
from models.ship import Ship
from models.technology import Technology
from models.dice import Dice
from models.constructable import Constructable
from database import (
    parts_db, blueprints_db, factions_db, players_db, reputation_tiles_db, sector_tiles_db, ships_db, technologies_db,
    faction_setup_functions_db
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
def read_part(part_id: str):
    for part in parts_db:
        if part.id == part_id:
            return part
    raise HTTPException(status_code=404, detail="Part not found")

@app.put("/parts/{part_id}", response_model=Part)
def update_part(part_id: str, part: Part):
    for i, part in enumerate(parts_db):
        if part.id == part_id:
            parts_db[i] = part
            return part
    raise HTTPException(status_code=404, detail="Part not found")

@app.delete("/parts/{part_id}", response_model=Part)
def delete_part(part_id: str):
    for i, part in enumerate(parts_db):
        if part.id == part_id:
            part = parts_db.pop(i)
            return part
    raise HTTPException(status_code=404, detail="Part not found")

# Blueprint Endpoints
@app.post("/blueprints/", response_model=Blueprint)
def create_blueprint(blueprint: Blueprint):
    blueprints_db.append(blueprint)
    return blueprint

@app.get("/blueprints/", response_model=List[Blueprint])
def read_blueprints():
    return blueprints_db

@app.get("/blueprints/{blueprint_id}", response_model=Blueprint)
def read_blueprint(blueprint_id: str):
    for blueprint in blueprints_db:
        if blueprint.id == blueprint_id:
            return blueprint
    raise HTTPException(status_code=404, detail="Blueprint not found")

@app.put("/blueprints/{blueprint_id}", response_model=Blueprint)
def update_blueprint(blueprint_id: str, blueprint: Blueprint):
    for i, blueprint in enumerate(blueprints_db):
        if blueprint.id == blueprint_id:
            blueprints_db[i] = blueprint
            return blueprint
    raise HTTPException(status_code=404, detail="Blueprint not found")

@app.delete("/blueprints/{blueprint_id}", response_model=Blueprint)
def delete_blueprint(blueprint_id: str):
    for i, blueprint in enumerate(blueprints_db):
        if blueprint.id == blueprint_id:
            blueprint = blueprints_db.pop(i)
            return blueprint
    raise HTTPException(status_code=404, detail="Blueprint not found")

# CRUD for Dice
@app.post("/dice/", response_model=Dice)
def create_dice(dice: Dice):
    dice_db.append(dice)
    return dice

@app.get("/dice/", response_model=List[Dice])
def read_dice():
    return dice_db

@app.get("/dice/{dice_id}", response_model=Dice)
def read_dice_by_id(dice_id: str):
    for dice in dice_db:
        if dice.id == dice_id:
            return dice
    raise HTTPException(status_code=404, detail="Dice not found")

@app.put("/dice/{dice_id}", response_model=Dice)
def update_dice(dice_id: str, dice: Dice):
    for i, d in enumerate(dice_db):
        if d.id == dice_id:
            dice_db[i] = dice
            return dice
    raise HTTPException(status_code=404, detail="Dice not found")

@app.delete("/dice/{dice_id}", response_model=Dice)
def delete_dice(dice_id: str):
    for i, d in enumerate(dice_db):
        if d.id == dice_id:
            return dice_db.pop(i)
    raise HTTPException(status_code=404, detail="Dice not found")

# CRUD for Constructable
@app.post("/constructables/", response_model=Constructable)
def create_constructable(constructable: Constructable):
    constructables_db.append(constructable)
    return constructable

@app.get("/constructables/", response_model=List[Constructable])
def read_constructables():
    return constructables_db

@app.get("/constructables/{constructable_id}", response_model=Constructable)
def read_constructable_by_id(constructable_id: str):
    for constructable in constructables_db:
        if constructable.id == constructable_id:
            return constructable
    raise HTTPException(status_code=404, detail="Constructable not found")

@app.put("/constructables/{constructable_id}", response_model=Constructable)
def update_constructable(constructable_id: str, constructable: Constructable):
    for i, c in enumerate(constructables_db):
        if c.id == constructable_id:
            constructables_db[i] = constructable
            return constructable
    raise HTTPException(status_code=404, detail="Constructable not found")

@app.delete("/constructables/{constructable_id}", response_model=Constructable)
def delete_constructable(constructable_id: str):
    for i, c in enumerate(constructables_db):
        if c.id == constructable_id:
            return constructables_db.pop(i)
    raise HTTPException(status_code=404, detail="Constructable not found")

# CRUD for Faction
@app.post("/factions/", response_model=Faction)
def create_faction(faction: Faction):
    factions_db.append(faction)
    return faction

@app.get("/factions/", response_model=List[Faction])
def read_factions():
    return factions_db

@app.get("/factions/{faction_id}", response_model=Faction)
def read_faction_by_id(faction_id: str):
    for faction in factions_db:
        if faction.id == faction_id:
            # run the setup function from the db
            faction_name = faction.setup_faction
            setup_function = faction_setup_functions_db[faction_name]
            player = players_db[0]
            setup_function(faction.id, player.id)
            return faction
    raise HTTPException(status_code=404, detail="Faction not found")

@app.put("/factions/{faction_id}", response_model=Faction)
def update_faction(faction_id: str, faction: Faction):
    for i, f in enumerate(factions_db):
        if f.id == faction_id:
            factions_db[i] = faction
            return faction
    raise HTTPException(status_code=404, detail="Faction not found")

@app.delete("/factions/{faction_id}", response_model=Faction)
def delete_faction(faction_id: str):
    for i, f in enumerate(factions_db):
        if f.id == faction_id:
            return factions_db.pop(i)
    raise HTTPException(status_code=404, detail="Faction not found")

# CRUD for SectorTile
@app.post("/sector_tiles/", response_model=SectorTile)
def create_sector_tile(sector_tile: SectorTile):
    sector_tiles_db.append(sector_tile)
    return sector_tile

@app.get("/sector_tiles/", response_model=List[SectorTile])
def read_sector_tiles():
    return sector_tiles_db

@app.get("/sector_tiles/{sector_tile_id}", response_model=SectorTile)
def read_sector_tile_by_id(sector_tile_id: str):
    for sector_tile in sector_tiles_db:
        if sector_tile.id == sector_tile_id:
            return sector_tile
    raise HTTPException(status_code=404, detail="SectorTile not found")

@app.put("/sector_tiles/{sector_tile_id}", response_model=SectorTile)
def update_sector_tile(sector_tile_id: str, sector_tile: SectorTile):
    for i, st in enumerate(sector_tiles_db):
        if st.id == sector_tile_id:
            sector_tiles_db[i] = sector_tile
            return sector_tile
    raise HTTPException(status_code=404, detail="SectorTile not found")

@app.delete("/sector_tiles/{sector_tile_id}", response_model=SectorTile)
def delete_sector_tile(sector_tile_id: str):
    for i, st in enumerate(sector_tiles_db):
        if st.id == sector_tile_id:
            return sector_tiles_db.pop(i)
    raise HTTPException(status_code=404, detail="SectorTile not found")

# CRUD for ReputationTile
@app.post("/reputation_tiles/", response_model=ReputationTile)
def create_reputation_tile(reputation_tile: ReputationTile):
    reputation_tiles_db.append(reputation_tile)
    return reputation_tile

@app.get("/reputation_tiles/", response_model=List[ReputationTile])
def read_reputation_tiles():
    return reputation_tiles_db

@app.get("/reputation_tiles/{reputation_tile_id}", response_model=ReputationTile)
def read_reputation_tile_by_id(reputation_tile_id: str):
    for reputation_tile in reputation_tiles_db:
        if reputation_tile.id == reputation_tile_id:
            return reputation_tile
    raise HTTPException(status_code=404, detail="ReputationTile not found")

@app.put("/reputation_tiles/{reputation_tile_id}", response_model=ReputationTile)
def update_reputation_tile(reputation_tile_id: str, reputation_tile: ReputationTile):
    for i, rt in enumerate(reputation_tiles_db):
        if rt.id == reputation_tile_id:
            reputation_tiles_db[i] = reputation_tile
            return reputation_tile
    raise HTTPException(status_code=404, detail="ReputationTile not found")

@app.delete("/reputation_tiles/{reputation_tile_id}", response_model=ReputationTile)
def delete_reputation_tile(reputation_tile_id: str):
    for i, rt in enumerate(reputation_tiles_db):
        if rt.id == reputation_tile_id:
            return reputation_tiles_db.pop(i)
    raise HTTPException(status_code=404, detail="ReputationTile not found")

# CRUD for Technology
@app.post("/technologies/", response_model=Technology)
def create_technology(technology: Technology):
    technologies_db.append(technology)
    return technology

@app.get("/technologies/", response_model=List[Technology])
def read_technologies():
    return technologies_db

@app.get("/technologies/{technology_id}", response_model=Technology)
def read_technology_by_id(technology_id: str):
    for technology in technologies_db:
        if technology.id == technology_id:
            return technology
    raise HTTPException(status_code=404, detail="Technology not found")


@app.put("/technologies/{technology_id}", response_model=Technology)
def update_technology(technology_id: str, technology: Technology):
    for i, t in enumerate(technologies_db):
        if t.id == technology_id:
            technologies_db[i] = technology
            return technology
    raise HTTPException(status_code=404, detail="Technology not found")


@app.delete("/technologies/{technology_id}", response_model=Technology)
def delete_technology(technology_id: str):
    for i, t in enumerate(technologies_db):
        if t.id == technology_id:
            return technologies_db.pop(i)
    raise HTTPException(status_code=404, detail="Technology not found")


# CRUD for Ship
@app.post("/ships/", response_model=Ship)
def create_ship(ship: Ship):
    ships_db.append(ship)
    return ship

@app.get("/ships/", response_model=List[Ship])
def read_ships():
    return ships_db

@app.get("/ships/{ship_id}", response_model=Ship)
def read_ship_by_id(ship_id: str):
    for ship in ships_db:
        if ship.id == ship_id:
            return ship
    raise HTTPException(status_code=404, detail="Ship not found")

@app.put("/ships/{ship_id}", response_model=Ship)
def update_ship(ship_id: str, ship: Ship):
    for i, s in enumerate(ships_db):
        if s.id == ship_id:
            ships_db[i] = ship
            return ship
    raise HTTPException(status_code=404, detail="Ship not found")

@app.delete("/ships/{ship_id}", response_model=Ship)
def delete_ship(ship_id: str):
    for i, s in enumerate(ships_db):
        if s.id == ship_id:
            return ships_db.pop(i)
    raise HTTPException(status_code=404, detail="Ship not found")

#CRUD for Player
@app.post("/players/", response_model=Player)
def create_player(player: Player):
    players_db.append(player)
    return player

@app.get("/players/", response_model=List[Player])
def read_players():
    return players_db

@app.get("/players/{player_id}", response_model=Player)
def read_player_by_id(player_id: str):
    for player in players_db:
        if player.id == player_id:
            return player
    raise HTTPException(status_code=404, detail="Player not found")

@app.put("/players/{player_id}", response_model=Player)
def update_player(player_id: str, player: Player):
    for i, p in enumerate(players_db):
        if p.id == player_id:
            players_db[i] = player
            return player
    raise HTTPException(status_code=404, detail="Player not found")

@app.delete("/players/{player_id}", response_model=Player)
def delete_player(player_id: str):
    for i, p in enumerate(players_db):
        if p.id == player_id:
            return players_db.pop(i)
    raise HTTPException(status_code=404, detail="Player not found")

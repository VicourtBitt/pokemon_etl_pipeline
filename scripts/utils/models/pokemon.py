from pydantic import BaseModel
from typing import List, Dict

class PokemonData(BaseModel):
    """
    This represents the data that cames from the API when you try to
    retrieve a Pokémon by its ID.
    """
    id: int
    order: int
    height: int
    weight: int
    is_default: bool
    name: str
    location_area_encounters: str
    cries: Dict
    species: Dict
    sprites: Dict
    stats: List[Dict]
    moves: List[Dict]
    types: List[Dict]
    forms: List[Dict]
    abilities: List[Dict]
    past_stats: List[Dict]
    past_types: List[Dict]
    held_items: List[Dict]
    game_indices: List[Dict]
    past_abilities: List[Dict]
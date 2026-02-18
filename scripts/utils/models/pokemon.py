from pydantic import BaseModel
from typing import List, Dict

class PokemonInfo(BaseModel):
    """
    This represents the info that cames from the API when you try to
    retrieve a Pokémon by its ID.
    """
    id: int
    height: int
    weight: int
    is_default: bool
    name: str
    stats: List[Dict]
    types: List[Dict]
    abilities: List[Dict]


class PokemonJsonData(BaseModel):
    """
    This represents the 'filtered' JSON
    """
    data: List[PokemonInfo]
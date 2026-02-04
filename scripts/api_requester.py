from scripts.utils.models.pokemon import PokemonData
from typing import List
import requests
import logging
import dotenv
import os

dotenv.load_dotenv()

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

_POKE_API_URL_ = os.getenv("POKE_API_URL")


def extract_pokemon(poke_code: int = None) -> PokemonData:
    """
    This function acts as a helper to gather one specific Pokémon, although, there's no parameter diversity
    on this one, as the main goal is to extract all possible useful information about the pokemon, and not
    only their name.

    It'll be used within the extract_spec_gen method, to extract all pokemons of a certain generation.
    
    :param poke_code: Represents the number (id) of a certain Pokémon in the Pokedex, Bulbasaur is the 1° one
                      as an example
    :type poke_code: int

    :return: A dict model that represents the Pokémon Data in question
    :rtype: PokemonData
    """
    if not poke_code:
        raise ValueError(f"There's no poke_code defined, you should define one to extract a pokemon.")
    
    response = requests.get(f"{_POKE_API_URL_}/{poke_code}")
    if response.status_code == 200:
        data = response.json()
        return PokemonData(**data)


def extract_spec_gen(generation: list = None) -> None | List[PokemonData]:
    """
    This function receives a list that represents all the numbers between the start/end of a certain
    Pokémon generation in question, this makes easier for us to gather Pokémon's from a certain 
    period/series.
    
    :param generation: The list that has all the ID's of a certain Pokémon generation
    :type generation: list[int]

    :return: A list that has all the relevant PokemonData from a certain generation 
    :rtype: List[PokemonData] | None
    """

    if not generation:
        _logger.error("No generation informed")
        raise ValueError("There should be a Pokémon Generation list to extract at least a Pokémon.")
    
    pokemon_list: List[PokemonData] = []
    for num in generation:
        poke_data = extract_pokemon(poke_code=num)
        if not poke_data:
            _logger.error("Pokémon has not been appended, there's no information.")
            raise ValueError("To append into the Pokémon list, we should at least have a any information about the Pokémon in question")
        
        pokemon_list.append(poke_data)
        msg_str = f"Finished to append {num}° — {poke_data.name} into the list."
        # print(msg_str)
        _logger.info(msg_str)

    return pokemon_list
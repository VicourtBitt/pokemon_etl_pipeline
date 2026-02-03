import requests
import dotenv
import os

# from const.generations import __FIRST_GEN__

dotenv.load_dotenv()

_POKE_API_URL_ = os.getenv("POKE_API_URL")

def get_gen_range(start, end):
    return list(range(start, end+1))

__FIRST_GEN__ = get_gen_range(1, 151)

def extract_pokemon(poke_code: int = None):
    if not poke_code:
        raise ValueError(f"There's no poke_code defined, you should define one to extract a pokemon.")
    
    response = requests.get(f"{_POKE_API_URL_}/{poke_code}")
    if response.status_code == 200:
        data = response.json()
        return data


def extract_spec_gen(generation: list = None):
    if not generation:
        raise ValueError("There should be a Pokémon Generation list to extract at least a Pokémon.")
    
    pokemon_list = []
    for num in generation:
        poke_data = extract_pokemon(poke_code=num)
        if not poke_data:
            raise ValueError("To append into the Pokémon list, we should at least have a any information about the Pokémon in question")
        pokemon_list.append(poke_data)
        print(f"Finished to append {num}° — {poke_data["name"]} into the list.")

    return pokemon_list

print(extract_spec_gen(__FIRST_GEN__))
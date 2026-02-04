from scripts.utils.const.generations import __FIRST_GEN__
from scripts.utils.models.pokemon import PokemonData
from scripts.api_requester import extract_spec_gen
from typing import Literal
import pandas as pd
import logging

_logger = logging.getLogger(__name__)

_POKEDATA_COLS_ = list(PokemonData.model_fields.keys())

def save_pokemons_into_file(filetype: Literal["parquet", "csv"]):
    poke_list = extract_spec_gen(__FIRST_GEN__)
    if not poke_list:
        # print("Pokelist shouldn't return as empty.")
        _logger.error("Pokelist shouldn't return as empty.")
        raise ValueError("The Pokémon List should have at least one PokeData register to work properly.")

    poke_dataframe = pd.DataFrame(poke_list, columns=_POKEDATA_COLS_)

    if filetype not in ("parquet", "csv"):
        # print("The file extension/type should be one of those two: [parquet, csv]")
        _logger.error("The file extension/type should be one of those two: [parquet, csv]")
        raise NameError("To continue with the extraction, you should have a parquet or csv extension selected")
    
    msg_str = f"File being exported to: {filetype}"
    if filetype == "parquet":
        poke_dataframe.to_parquet("data/extracted_pokemon.parquet")

    elif filetype == "csv":
        poke_dataframe.to_csv("data/extracted_pokemon.csv")

    # print(msg_str)
    _logger.info(msg_str)    
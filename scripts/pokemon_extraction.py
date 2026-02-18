from scripts.utils.const.generations import __FIRST_GEN__
from scripts.utils.models.pokemon import PokemonInfo, PokemonJsonData
from scripts.api_requester import extract_spec_gen
from typing import Literal
import pandas as pd
import logging

_logger = logging.getLogger(__name__)

_POKEDATA_COLS_ = list(PokemonInfo.model_fields.keys())


def save_pokemon_to_raw():
    # print("Getting RAW pokemon data")
    _logger.info("Getting RAW pokemon data")
    poke_list : PokemonJsonData = extract_spec_gen(__FIRST_GEN__)
    poke_dataframe = pd.DataFrame(poke_list.data, columns=_POKEDATA_COLS_)
    # print("Saving RAW pokemon data")
    _logger.info("Saving RAW pokemon data")
    poke_dataframe.to_json(f"data/raw/pokemon_raw_data.json")
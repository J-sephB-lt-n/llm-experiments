import itertools
import logging
import math
import random
import re
import sys
from typing import Final

from src.obj import Location
from src.llm import Llm
from src.prompting.prompt_generator import PromptGenerator
from src.string_cleaning import remove_punctuation

logger = logging.getLogger(__name__)


def generate_locations(
    n_locations: int, prompt_generator: PromptGenerator, llm: Llm
) -> list[Location]:
    logger.info("Generating location names")
    prompt: str = prompt_generator.generate_location_names(n_locations)
    logger.debug('Prompt:\n"%s"', prompt)
    raw_response: str = llm.respond(prompt)
    location_strings: list[str] = [
        remove_punctuation(x) for x in re.split(r"\d+", raw_response) if len(x) > 5
    ]
    logger.info("Generating location objects")
    unjoined_locations: list[Location] = [
        Location(location_name) for location_name in location_strings
    ]
    if len(unjoined_locations) != n_locations:
        logger.warning(
            "Requested %s locations but parsed %s locations from LLM response",
            n_locations,
            len(locations),
        )

    logger.info("Joining locations to one another")
    random.shuffle(unjoined_locations)
    MAX_N_EDGES_PER_LOCATION: Final[int] = 3
    CREATE_NEW_EDGE_PROB: Final[float] = 1.0
    current_location: Location = unjoined_locations.pop(0)
    counter = itertools.count()
    while len(unjoined_locations) > 0:
        logger.debug("joining locations: iteration %s", f"{next(counter):,}")
        if len(current_location.adjacent_locations) >= MAX_N_EDGES_PER_LOCATION or (
            len(current_location.adjacent_locations) > 0
            and random.uniform(0, 1) > CREATE_NEW_EDGE_PROB
        ):
            current_location = random.choice(current_location.adjacent_locations)
        else:
            location_to_join: Location = unjoined_locations.pop(0)
            current_location.adjacent_locations.append(location_to_join)
            location_to_join.adjacent_locations.append(current_location)

    return current_location

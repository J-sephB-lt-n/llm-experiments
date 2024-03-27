"""
The entrypoint for this project

Example script usage:
    $ python main.py --logging_level DEBUG
"""

import argparse
import json
import logging
import random

import config
import src.game_state
import src.llm
import src.obj
import src.prompting
import src.world_creation

parser = argparse.ArgumentParser()
parser.add_argument(
    # an optional boolean flag
    "-l",
    "--logging_level",
    help="Value passed to `level` argument of logging.basicConfig()",
    default="INFO",
    type=str,
)
args = parser.parse_args()

logging.basicConfig(
    level=getattr(logging, args.logging_level),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    prompt_generator = src.prompting.PromptGenerator()
    cleaning_prompt_generator = src.prompting.CleaningPromptGenerator()
    llm = src.llm.OllamaLlm("mistral")
    prompt_generator.set_global_story_style()
    logger.debug(json.dumps(prompt_generator.parts, indent=4))
    current_location: src.obj.Location = src.world_creation.generate_locations(
        n_locations=config.N_LOCATIONS, prompt_generator=prompt_generator, llm=llm
    )
    player_choice = None
    while player_choice != "exit":
        current_location, player_choice = src.game_state.update_game_state(
            current_location=current_location,
            prompt_generator=prompt_generator,
            llm=llm,
        )

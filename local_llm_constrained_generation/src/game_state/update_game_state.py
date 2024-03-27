import logging

from src.obj import Location
from src.llm import Llm
from src.prompting.prompt_generator import PromptGenerator

logger = logging.getLogger(__name__)


def update_game_state(
    current_location: Location, prompt_generator: PromptGenerator, llm: Llm
):
    """Renders current game state,
    gets user input,
    and returns updated game state
    """
    if current_location.description is None:
        prompt: str = prompt_generator.generate_location_description(
            current_location.name
        )
        logger.debug('Prompt:\n"%s"', prompt)
        current_location.description = llm.respond(prompt)
    print("\033c", end="", flush=True)  # clear terminal
    print(
        f"""-- Current location --
[{current_location.name}]
{current_location.description}
    """
    )

    print("The following options are available to you:")
    for idx, location in enumerate(current_location.adjacent_locations):
        print(f'    Enter "{idx}" to travel to new location [{location.name}]')
    print('    Enter "exit" to leave the game')
    print("    Any other text you submit will be interpreted as your action")
    print('        e.g. "I close my eyes and shout as loud as I can"')

    player_choice: str = input("Please choose an action: ")
    if player_choice.isdigit():
        return current_location.adjacent_locations[int(player_choice)], player_choice

    if player_choice != "exit":
        prompt: str = prompt_generator.generate_response_to_user_action(
            location_name=current_location.name,
            location_description=current_location.description,
            user_action_description=player_choice,
        )
        logger.debug('Prompt:\n"%s"', prompt)
        location_response_to_user_action: str = llm.respond(prompt)
        print(location_response_to_user_action)
        _: str = input("Please press enter to continue")
        prompt: str = prompt_generator.user_action_updates_location_description(
            location_name=current_location.name,
            location_description=current_location.description,
            user_action_description=player_choice,
            location_response_to_user_action=location_response_to_user_action,
        )
        logger.debug('Prompt:\n"%s"', prompt)
        current_location.description = llm.respond(prompt)

    return current_location, player_choice

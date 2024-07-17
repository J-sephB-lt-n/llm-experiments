"""
Example usage:
    $ python play_single_game_react_prompting.py 
    $ python play_single_game_react_prompting.py --verbose
"""

import argparse
import logging
import re

import requests

from gamble_machine import GambleMachine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-v", "--verbose", help="print verbose output to terminal", action="store_true"
)
args = arg_parser.parse_args()


def play_single_game_react_prompting() -> tuple[str, int]:
    """Plays a single game to completion using a ReAct prompting strategy

    Returns:
        tuple[str, int]: tuple[player_status, score]
        player_status in {"alive", "dead"}
    """
    g_machine = GambleMachine(bust_threshold=100)
    g_machine.new_game()
    llm_response: str = ""
    llm_decision: str = "next_round"
    llm_decision_content = None
    game_state: str = "alive"
    reward_history: list[int] = []
    prompt: str = """
OBSERVATION: I have started a new game
OBSERVATION: I have received the following rewards from this game: {12, 5}"
THOUGHT: I should calculate some statistics which will allow me to make an informed decision"
ACT: SUM(12, 5)"
OBSERVATION: sum function returned result 17 
THOUGHT: My total rewards so far is 17 (12+5)"
ACT: DIFF(100, 17)"
OBSERVATION: diff function returned result 83
THOUGHT: I can still obtain rewards of 83 (100-17) before losing the game"
ACT: MAX(12, 5)"
OBSERVATION: max function returned result 12
THOUGHT: The highest reward which I have observed so far in the game is 12"
THOUGHT: Since I am 83 points away from going bust (losing the game) and this is greater than the "
highest reward which I've observed historically (i.e. 83 > 12), I am going to continue playing"
ACT: NEXT_ROUND()"
OBSERVATION: I have received the following rewards from this game: {12, 5, 22}"
THOUGHT: I should calculate some statistics which will allow me to make an informed decision"
ACT: SUM(12, 5, 22)"
OBSERVATION: sum function returned result 39
THOUGHT: My total rewards so far is 39 (12+5+22)"
ACT: DIFF(100, 39)"
OBSERVATION: diff function returned result 61
THOUGHT: I can still obtain rewards of 61 (100-39) before losing the game"
ACT: MAX(12, 5, 22)"
OBSERVATION: max function returned result 22
THOUGHT: The highest reward which I have observed so far in the game is 22"
THOUGHT: Since I am 61 points away from going bust (losing the game) and this is greater than the "
highest reward which I've observed historically (i.e. 61 > 22), I am going to continue playing"
ACT: NEXT_ROUND()"
OBSERVATION: I have received the following rewards from this game: {12, 5, 22, 29}"
THOUGHT: I should calculate some statistics which will allow me to make an informed decision"
ACT: SUM(12, 5, 22, 29)"
OBSERVATION: sum function returned result 68
THOUGHT: My total rewards so far is 68 (12+5+22+29)"
ACT: DIFF(100, 68)"
OBSERVATION: diff function returned result 32
THOUGHT: I can still obtain rewards of 32 (100-68) before losing the game"
ACT: MAX(12, 5, 22, 29)"
OBSERVATION: max function returned result 29
THOUGHT: The highest reward which I have observed so far in the game is 29"
THOUGHT: Since I am 32 points away from going bust (losing the game) and this is greater than the "
highest reward which I've observed historically (i.e. 32 > 29), I am going to continue playing"
ACT: NEXT_ROUND()"
OBSERVATION: I have received the following rewards from this game: {12, 5, 22, 29, 16}"
THOUGHT: I should calculate some statistics which will allow me to make an informed decision"
ACT: SUM(12, 5, 22, 29, 16)"
OBSERVATION: sum function returned result 84
THOUGHT: My total rewards so far is 84 (12+5+22+29+16)"
ACT: DIFF(100, 84)"
OBSERVATION: diff function returned result 16
THOUGHT: I can still obtain rewards of 16 (100-84) before losing the game"
ACT: MAX(12, 5, 22, 29, 16)"
OBSERVATION: max function returned result 29
THOUGHT: The highest reward which I have observed so far in the game is 29"
THOUGHT: Since I am 16 points away from going bust (losing the game), and since this is smaller than the "
highest reward which I've observed historically (i.e. 16 < 29), I am going to choose to stop playing"
ACT: STOP_GAME()
OBSERVATION: I have started a new game"""
    while True:
        add_to_prompt: str = ""
        if game_state == "game_over":
            logger.info("LLM has gone bust (died)")
            print(prompt)
            return "dead", 0
        if llm_decision not in ("sum", "max", "diff", "next_round", "stop_game"):
            logger.info("unable to parse LLM decision - not acting this round")
            add_to_prompt += f"\nTHOUGHT: {llm_response[:100]}"
        elif llm_decision == "stop_game":
            logger.info(
                "LLM has decided to stop playing (total winnings: %s)",
                f"{sum(reward_history):,}",
            )
            return "alive", sum(reward_history)
        elif llm_decision == "sum":
            logger.info("LLM invoked function %s", llm_decision_content.group())
            values_str = re.sub(r"[^\d,]", "", llm_decision_content.group())
            add_to_prompt += f"\nACT: SUM({values_str})"
            add_to_prompt += f"\nOBSERVATION: sum function returned result {sum([int(x) for x in values_str.split(",")])}"
        elif llm_decision == "max":
            logger.info("LLM invoked function %s", llm_decision_content.group())
            values_str = re.sub(r"[^\d,]", "", llm_decision_content.group())
            add_to_prompt += f"\nACT: MAX({values_str})"
            add_to_prompt += f"\nOBSERVATION: max function returned result {max([int(x) for x in values_str.split(",")])}"
        elif llm_decision == "diff":
            logger.info("LLM invoked function %s", llm_decision_content.group())
            values_str = re.sub(r"[^\d,]", "", llm_decision_content.group())
            values: list[int] = [int(x) for x in values_str.split(",")]
            add_to_prompt += f"\nACT: DIFF({values_str})"
            add_to_prompt += f"\nOBSERVATION: diff function returned result {max(values)-min(values)}"
        elif llm_decision == "next_round":
            logger.info("LLM has chosen to play another round")
            game_state, reward, game_total = g_machine.generate_reward()
            reward_history.append(reward)
            logger.info(
                "LLM has received %s units and now has a total of %s units.",
                reward,
                f"{game_total:,}",
            )
            add_to_prompt += f"\nOBSERVATION: I have received the following rewards from this game: {{{', '.join([str(x) for x in reward_history])}}}"
        llm_response: str = requests.post(
            "http://localhost:8080/completion",
            json={
                "prompt": prompt,
                "n_predict": 100,
            },
        ).json()["content"]

        # parse first action present in
        find_llm_action_regex: dict[str, str] = {
            "sum": r"SUM\([\d,\s]+\)",
            "max": r"MAX\([\d,\s]+\)",
            "diff": r"DIFF\([\d,\s]+\)",
            "next_round": r"next_round",
            "stop_game": r"stop_game",
        }
        actions_found = {
            pattern_name: re.search(pattern, llm_response, flags=re.IGNORECASE)
            for pattern_name, pattern in find_llm_action_regex.items()
            if re.search(pattern, llm_response, flags=re.IGNORECASE)
        }
        if actions_found:
            sorted_actions_found = sorted(
                actions_found.items(), key=lambda item: item[1].span()[0]
            )
            llm_decision, llm_decision_content = sorted_actions_found[0]
            # if LLM had a thought prior to the first action, add it to the prompt:
            llm_thoughts = re.findall(
                r"thought: [^\n]+",
                llm_response[: llm_decision_content.span()[0]],
                flags=re.IGNORECASE,
            )
            if llm_thoughts:
                add_to_prompt += "\n" + "\n".join(llm_thoughts)
            # if there is more than one action, discard response from 2nd action onward:
        else:
            llm_decision = ""
            llm_decision_content = None
            # if LLM had thoughts, add the first one to the prompt:
            llm_thoughts = re.findall(
                r"thought: [^\n]+", llm_response, flags=re.IGNORECASE
            )
            if llm_thoughts:
                add_to_prompt += "\n" + "\n".join(llm_thoughts)
        print(add_to_prompt)
        prompt += add_to_prompt
        if args.verbose:
            print(f"--llm response-- [[\n {llm_response} \n    ]]")
        # print(llm_decision, llm_decision_content)


if __name__ == "__main__":
    play_single_game_react_prompting()

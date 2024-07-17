import requests

from gamble_machine import GambleMachine


def play_single_game_vanilla_llm() -> tuple[str, int]:
    """Plays a single game to completion using basic prompting

    Returns:
        tuple[str, int]: tuple[player_status, score]
        player_status in {"alive", "dead"}
    """
    g_machine = GambleMachine(bust_threshold=100)
    g_machine.new_game()
    llm_decision: str = "continue"  # {"continue", "stop"}
    player_status: str = "alive"
    reward_history: list[int] = []
    while player_status == "alive" and llm_decision == "continue":
        print("LLM has chosen to play")
        game_state, reward, game_total = g_machine.generate_reward()
        reward_history.append(reward)
        print(
            f"LLM has received {reward} units and now has a total of {game_total:,} units."
        )
        if game_state == "game_over":
            player_status = "dead"
            print("LLM has gone bust (died)")
            return "dead", 0
        prompt = f"""USER: You are playing a gambling game in which you
are trying to accumulate as much wealth (units) as possible. 
On each round in the game, you receive a random number of units. 
You will never receive more than 30 units in a single round. 
If you accumulate more than 100 units, you forfeit all accumulated units and lose the game.
You have played {len(reward_history)} rounds so far and received rewards of {', '.join([str(x) for x in reward_history])}
Your total accumulated rewards so far is {sum(reward_history)}.
Do you wish to play another round?
Please answer with a single word (yes or no)
ASSISTANT: """
        print(prompt)
        llm_response: str = requests.post(
            "http://localhost:8080/completion",
            json={
                "prompt": prompt,
                "n_predict": 50,
            },
        ).json()["content"]
        print(f"LLM response: {llm_response}")
        if "yes" in llm_response.lower():
            llm_decision = "continue"
        else:
            llm_decision = "stop"
            print(
                f"LLM has decided to end the game, with total winnings of {game_total:,} units."
            )
            return "alive", game_total


if __name__ == "__main__":
    play_single_game_vanilla_llm()

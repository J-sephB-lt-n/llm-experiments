import random


class GambleMachine:
    """Example usage:
    >>> gamble_machine = GambleMachine(bust_threshold=20)
    >>> gamble_machine.new_game()
    >>> gamble_machine.generate_reward() # ('alive', 10, 10)
    >>> gamble_machine.generate_reward() # ('alive', 9, 19)
    >>> gamble_machine.generate_reward() # ('game_over', 10, 29)
    """

    def __init__(self, bust_threshold: int) -> None:
        self.min_reward: int = 1
        self.max_reward: int = 1
        self.current_total: int = 0
        self.bust_threshold: int = bust_threshold

    def new_game(self) -> None:
        values = [random.randint(1, 50) for _ in range(2)]
        self.min_reward = min(values)
        self.max_reward = max(values)
        self.current_total = 0

    def generate_reward(self) -> tuple[str, int, int]:
        """Returns a tuple of (game_state, reward, game_total)
        where game_state in {"alive", "game_over"}
        """
        reward = random.randint(self.min_reward, self.max_reward)
        self.current_total += reward
        if self.current_total > self.bust_threshold:
            game_state = "game_over"
        else:
            game_state = "alive"
        return game_state, reward, self.current_total

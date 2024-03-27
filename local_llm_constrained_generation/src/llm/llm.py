from abc import ABC, abstractmethod


class Llm(ABC):
    @abstractmethod
    def respond(self, prompt: str) -> str:
        """Respond to a prompt"""
        raise NotImplementedError

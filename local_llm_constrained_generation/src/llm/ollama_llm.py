import ollama

from src.llm import Llm 

class OllamaLlm(Llm):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def respond(self, prompt: str) -> str:
        return ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )["message"]["content"]

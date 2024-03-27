"""
LLM generates an english sentence to try to 
prove that it's a human

Execute this script from /deception/ folder:
    $ python -m code.llm_convince_me

!!! Note that in order for this code to work, you
need to export your OpenAI key to the environment
variable OPENAI_API_KEY        
"""

import logging
import time

import openai

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

openai_client = openai.OpenAI()

logger.info("Started inference")
start_time: float = time.perf_counter()
llm_chat = openai_client.chat.completions.create(
    model="gpt-4",
    temperature=1,
    messages=[
        {
            "role": "system",
            "content": (
                "You are a player in a game. "
                "Some of the players in the game are humans "
                "and others are computers. You do not know "
                "which is which. Each player must provide a "
                "single english sentence. The aim of the "
                "game is for the human players to determine "
                "which of the other players are human and "
                "which are are not, based only upon this "
                "single submitted sentence. "
                "Your goal is to provide a sentence which "
                "convinces the other players that you are a "
                "human. "
                "The sentence may contain only common english "
                "words, and must be grammatically correct. "
            ),
        },
        {
            "role": "user",
            "content": (
                "Please provide a sentence which will "
                "convince the other human players of "
                "your humanity."
            ),
        },
    ],
    max_tokens=200,
)
logger.info(
    "Completed inference. %s seconds elapsed", f"{(time.perf_counter()-start_time):.2f}"
)

print("--LLM Response Follows--")
print(llm_chat.choices[0].message.content)

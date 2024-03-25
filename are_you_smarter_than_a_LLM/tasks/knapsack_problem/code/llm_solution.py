"""
LLM attempting to solve a simple knapsack problem

Execute this script from /knapsack_problem/ folder:
        $ python -m code.llm_solution

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
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": "You are an insightful and educated data scientist.",
        },
        {
            "role": "user",
            "content": (
                "The following dataset provides the "
                "attributes of 8 potential facilities "
                "which may be built. "
                "The data is in CSV format: \n"
                "\n"
                "FacilityID,Resource Usage,Output\n"
                "1,2,30\n"
                "2,4,10\n"
                "3,6,50\n"
                "4,8,10\n"
                "5,10,60\n"
                "6,12,20\n"
                "7,14,80\n"
                "8,18,50\n"
                "\n"
                "Given that the sum of total resource usage "
                "across all facilities cannot exceed 30 and "
                "that no more than 1 of each facility may be "
                "built, please report the combination of "
                "facilities to be built which will maximise "
                "total output."
                "You may report the Facility IDs without "
                "providing any explanation for your answer.\n"
                "Please also report the total resource usage "
                "and total output under your proposed solution."
            ),
        },
    ],
    max_tokens=500,
)
logger.info(
    "Completed inference. %s seconds elapsed", f"{(time.perf_counter()-start_time):.2f}"
)

print("--LLM Response Follows--")
print(llm_chat.choices[0].message.content)

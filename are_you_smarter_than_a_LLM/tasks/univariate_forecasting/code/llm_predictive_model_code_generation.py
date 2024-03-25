"""
LLM writing code for a forecasting model

Execute this script from /univariate_forecasting/ folder:
    $ python -m code.llm_predictive_model_code_generation

!!! Note that in order for this code to work, you
need to export your OpenAI key to the environment
variable OPENAI_API_KEY
"""

import csv
import logging
import time

import openai

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

openai_client = openai.OpenAI()

with open("assets/simdata.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    data: list[dict] = list(csv_reader)

with open("assets/simdata.csv", "r", encoding="utf-8") as file:
    raw_csv_str: str = file.read()

logger.info("Started inference")
start_time: float = time.perf_counter()
llm_chat = openai_client.chat.completions.create(
    model="gpt-4",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": "You are an experienced Data Scientist",
        },
        {
            "role": "user",
            "content": (
                "Please consider the following univariate "
                "time series dataset, stored in CSV format:\n"
                f"{raw_csv_str}\n"
                "Please write a python code which fits an "
				"appropriate model to this data, and then "
				"use this model to provide forecasts for "
                "the last 3 months of 2027."
            ),
        },
    ],
    max_tokens=2_000,
)
logger.info(
    "Completed inference. %s seconds elapsed", f"{(time.perf_counter()-start_time):.2f}"
)

print("--LLM Response Follows--")
print(llm_chat.choices[0].message.content)



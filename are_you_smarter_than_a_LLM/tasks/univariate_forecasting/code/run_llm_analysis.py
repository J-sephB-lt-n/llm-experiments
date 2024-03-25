"""
Answers questions related to univariate time series
data using a Large Language Model

Execute this script from /univariate_forecasting/ folder:
    $ python -m code.run_llm_analysis

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
            "content": "You are an insightful and educated data analyst.",
        },
        {
            "role": "user",
            "content": (
                "Please consider the following univariate "
                "time series dataset, stored in CSV format:\n"
                f"{raw_csv_str}\n"
                "Please can you do the following:\n"
                "\t1. Describe any predictable patterns which "
                "you observe in this data (e.g. trend).\n"
                "\t2. Provide predictions (forecasted sales) "
                "for the last 3 months of 2027."
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

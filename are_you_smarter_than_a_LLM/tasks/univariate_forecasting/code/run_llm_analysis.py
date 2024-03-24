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

import openai

openai_client = openai.OpenAI()

with open("assets/simdata.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    raw_data: list[dict] = list(csv_reader)



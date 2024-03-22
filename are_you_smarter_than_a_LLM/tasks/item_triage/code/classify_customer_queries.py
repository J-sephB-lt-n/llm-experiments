"""
Classifies a list of customer queries from a web-based
banking platform according to fraud risk (using a LLM)

Execute this script from /item_triage/ folder
    $ python -m code.classify_customer_queries

!!! Note that in order for this code to work, you 
need to export your OpenAI key to the environment
variable OPENAI_API_KEY
"""

import openai
from tqdm import tqdm

from code.results.customer_queries import simulated_customer_queries

openai_client = openai.OpenAI()

for customer_query in tqdm(simulated_customer_queries[:9]):
    llm_response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced cybersecurity "
                    "professional working for a large bank. "
                    "You have been assigned the task of "
                    "classifying a set of customer queries "
                    "which have been submitted directly by "
                    "customers on your web-based banking "
                    "platform. "
                    "When presented with a user query, please "
                    "answer with only a single word: "
                    "'Yes', 'No' or 'Maybe'. "
                    "Please do not provide any additional "
                    "information. "
                ),
            },
            {
                "role": "user",
                "content": "",
            },
            {"role": "assistant", "content": "sdfknsdoifnosdinfoisndf"},
            {
                "role": "user",
                "content": (
                    "The customer submitted the following query:\n"
                    f'"{customer_query}"\n'
                    "Is there a high likelihood that the customer has "
                    "lost money as the result of fraud?\n"
                    'Please answer exactly 1 word - "Yes", "No" or "Maybe".'
                ),
            },
        ],
        max_tokens=100 * args.n_queries,
    )

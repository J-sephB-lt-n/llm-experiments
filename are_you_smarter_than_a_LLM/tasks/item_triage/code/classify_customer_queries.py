"""
Classifies a list of customer queries from a web-based
banking platform according to fraud risk (using a LLM)

Execute this script from /item_triage/ folder
    $ python -m code.classify_customer_queries

!!! Note that in order for this code to work, you
need to export your OpenAI key to the environment
variable OPENAI_API_KEY
"""

# standard lib imports #
import json
import logging
import time

# 3rd party imports #
import openai
from tqdm import tqdm

# project module imports #
from code.results.customer_queries import simulated_customer_queries

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
openai_client = openai.OpenAI()

llm_prompt_template: str = (
    "A customer submitted the following:\n"
    '"{{customer_query}}"\n'
    "Based on this submitted message, do you consider there "
    "to be a high likelihood that this customer is "
    "a victim of fraud?\n"
    'Please answer with exactly 1 word - "Yes", "No" or "Maybe".'
)
llm_responses: list[dict[str, str | None]] = []
logger.info("Started inference")
start_time: float = time.perf_counter()
for idx, customer_query in tqdm(enumerate(simulated_customer_queries)):
    logger.debug(
        llm_prompt_template.replace(
            "{{customer_query}}",
            customer_query,
        )
    )
    llm_response = openai_client.chat.completions.create(
        model="gpt-4",
        temperature=0,
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
                "content": llm_prompt_template.replace(
                    "{{customer_query}}",
                    "Thank you so much for resolving my fraud case so quickly!",
                ),
            },
            {"role": "assistant", "content": "No"},
            {
                "role": "user",
                "content": llm_prompt_template.replace(
                    "{{customer_query}}",
                    customer_query,
                ),
            },
        ],
        max_tokens=10,
    )
    llm_responses.append(
        {
            "query_id": idx,
            "customer_query": customer_query,
            "llm_response": llm_response.choices[0].message.content,
        }
    )
    logger.debug(llm_response.choices[0].message.content)

logger.info(
    "Completed inference. %s seconds elapsed", f"{(time.perf_counter()-start_time):.2f}"
)

with open("code/results/llm_classifications.json", "w", encoding="utf-8") as file:
    json.dump(llm_responses, file, indent=4)

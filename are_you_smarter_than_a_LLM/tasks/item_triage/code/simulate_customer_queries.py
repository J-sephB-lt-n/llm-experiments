"""
Code for simulating customer queries to a web-base banking
application using a Large Language Model

Example usage (run from folder /item_triage/):
    $ python -m code.simulate_customer_queries \
        --topic "fraudulent payments" \
        --n_queries 10

!!! Note that in order for this code to work, you 
need to export your OpenAI key to the environment
variable OPENAI_API_KEY
"""

# standard lib imports #
import argparse
import logging
import time

# 3rd party imports #
import openai

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--topic",
    help="The topic to generate queries about (this is inserted into the LLM prompt)",
    required=True,
    type=str,
)
parser.add_argument(
    "-n",
    "--n_queries",
    help="Number of queries to generate",
    required=True,  # this command line argument is required. The default value for is False
    type=int,
)
args = parser.parse_args()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

openai_client = openai.OpenAI()

llm_prompt: str = (
    f"Please generate {args.n_queries} authentic "
    "customer queries that were submitted to "
    "the 'customer support' service of a "
    "web-based banking application. "
    "Each query should be between 5 and 50 "
    "words long. The customer queries must "
    f"all be related to {args.topic}."
)
logger.info("Prompt:\n%s", llm_prompt)

logger.info("Calling LLM")
start_time: float = time.perf_counter()
llm_response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": llm_prompt,
        },
    ],
    max_tokens=100 * args.n_queries,
)
logger.info(
    "Received response from LLM. Total seconds elapsed: '%s'",
    f"{(time.perf_counter()-start_time):.2f}",
)

print(llm_response.choices[0].message.content)

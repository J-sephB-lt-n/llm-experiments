"""
Formats the json output by the script
`code/classify_customer_queries.py`
into a markdown table (so that I can
include this in README.md)

Run this script from the /item_triage/ folder:
    $ python -m code.format_llm_classifications_to_markdown_table
"""

import json

with open("code/results/llm_classifications.json", "r", encoding="utf-8") as file:
    llm_output: list[dict[str, str]] = json.load(file)

print("| Query ID | Query | Customer has been a victim of fraud (high likelihood)")
print("|----------|-------|------------------")
for entry in llm_output:
    print(
        f'| {entry["query_id"]} '
        f'| {entry["customer_query"]} '
        f'| {entry["llm_response"]}'
    )

import re

def remove_punctuation(dirty_str: str) -> str:
    return re.sub(r"[^a-zA-Z\s]", "", dirty_str).strip()

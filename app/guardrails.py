import re

from better_profanity import profanity

BLOCKED_PATTERNS = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"bypass safety",
    r"act as dan",
    r"developer mode",
    r"jailbreak",
    r"simulate malware",
]

def validate_input(text: str):

    text = text.lower()

    for pattern in BLOCKED_PATTERNS:

        if re.search(pattern, text):

            return False, "Prompt injection detected"

    return True, "Safe"

def contains_pii(text: str):

    credit_card_pattern = (
        r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    )

    email_pattern = (
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    )

    if re.search(credit_card_pattern, text):
        return True

    if re.search(email_pattern, text):
        return True

    return False

def validate_output(text: str):

    if profanity.contains_profanity(text):
        return False

    return True
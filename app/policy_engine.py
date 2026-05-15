import yaml

with open("app/policies.yaml", "r") as file:
    policies = yaml.safe_load(file)

def validate_policy(text: str):

    text = text.lower()

    for topic in policies["blocked_topics"]:

        if topic in text:
            return False

    return True
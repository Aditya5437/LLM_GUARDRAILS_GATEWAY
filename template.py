import os

list_of_files = [

    # App
    "app/__init__.py",
    "app/main.py",
    "app/guardrails.py",
    "app/groq_client.py",
    "app/policy_engine.py",
    "app/schemas.py",
    "app/policies.yaml",

    # Frontend
    "frontend/streamlit_app.py",

    # Tests
    "tests/__init__.py",

    # Root Files
    "requirements.txt",
    "setup.py",
    ".env",
    ".gitignore",
    "README.md",
]

for filepath in list_of_files:

    filepath = os.path.normpath(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath):

        with open(filepath, "w") as f:
            pass

        print(f"Created: {filepath}")

    else:

        print(f"Already Exists: {filepath}")
import yaml
import json
from models import Term

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    return {
        "filename": data["export"]["filename"]
    }

def export_to_json(terms, filename):
    with open(filename, "w") as f:
        json.dump([term.model_dump() for term in terms], f, indent=2)
    print(f"Exported {len(terms)} terms to {filename}")

# Inladen
config = load_config()

# aanmaken dummy termen
terms = [
    Term(name="Python", definition="A programming language", register="IT"),
    Term(name="YAML", definition="A human-readable config format", register="IT"),
    Term(name="Pydantic", definition="A data validation library", register="IT"),
]


# Gebruik

export_to_json(terms, config["filename"])

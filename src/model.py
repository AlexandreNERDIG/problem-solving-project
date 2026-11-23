import json

def load_instance(filepath):
    """Load a knapsack instance from a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data["name"], data["capacity"], data["items"]
import json
import random

def generate_knapsack(n, capacity, seed):
    rng = random.Random(seed)
    items = []
    for i in range(n):
        weight = rng.randint(1, 25)
        value = weight * rng.randint(2, 5) + rng.randint(0, 10) # Correlated for a bit more realism
        items.append({"id": i, "weight": weight, "value": value})
    return {
        "name": f"knapsack-n{n}-s{seed}",
        "capacity": capacity,
        "items": items
    }

for n in (100, 500, 1000):
    capacity = n * 10  # Capacity proportional to the number of items
    instance = generate_knapsack(n, capacity, seed=42)
    with open(f"data/medium/knapsack-n{n}.json", "w") as f:
        json.dump(instance, f, indent=2)

print("Medium Knapsack instances successfully generated!")
def greedy_knapsack(items, capacity):
    """Greedy algorithm: sorts items by decreasing value-to-weight ratio and takes the best ones."""
    # Calculate the ratio for each item
    rated_items = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)
    
    chosen = []
    current_weight = 0
    
    for item in rated_items:
        if current_weight + item["weight"] <= capacity:
            chosen.append(item["id"])
            current_weight += item["weight"]
            
    return chosen
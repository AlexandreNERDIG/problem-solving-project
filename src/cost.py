def total_value(items, chosen):
    """Calculate the total value of the selected items for the truck."""
    return sum(items[i]["value"] for i in chosen)

def is_feasible(items, capacity, chosen):
    """Check if the selection respects the truck capacity and does not take the same item twice."""
    # No duplicates in chosen IDs and total weight less than or equal to capacity
    weight = sum(items[i]["weight"] for i in chosen)
    return len(set(chosen)) == len(chosen) and weight <= capacity
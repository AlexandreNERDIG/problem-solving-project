from src.cost import total_value, is_feasible

ITEMS = [
    {"id": 0, "weight": 5, "value": 10},
    {"id": 1, "weight": 4, "value": 40},
    {"id": 2, "weight": 6, "value": 30},
    {"id": 3, "weight": 3, "value": 50}
]
CAPACITY = 10

def test_known_solution_value():
    # If we choose items 1 and 3: weight = 4 + 3 = 7 (<= 10), value = 40 + 50 = 90
    chosen = [1, 3]
    assert is_feasible(ITEMS, CAPACITY, chosen) == True
    assert total_value(ITEMS, chosen) == 90

def test_infeasible_solution_overweight():
    # If capacity is exceeded (items 0, 1 and 2 -> weight = 5+4+6 = 15 > 10)
    chosen = [0, 1, 2]
    assert is_feasible(ITEMS, CAPACITY, chosen) == False
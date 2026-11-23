from src.model import load_instance
from src.algorithms import greedy_knapsack
from src.cost import total_value, is_feasible
import matplotlib.pyplot as plt

def main():
    # Load a small or medium instance
    filepath = "data/small/knapsack-01.json"
    name, capacity, items = load_instance(filepath)
    
    print(f"--- Instance : {name} (Capacity: {capacity}) ---")
    
    # Exécuter l'algorithme
    solution = greedy_knapsack(items, capacity)
    print(f"Chosen items (IDs): {solution}")
    
    # Vérifier et évaluer
    feasible = is_feasible(items, capacity, solution)
    value = total_value(items, solution)
    
    print(f"Is it valid? {feasible}")
    print(f"Total transported value: {value}")

    # Petit bonus optionnel avec matplotlib (Graphique des objets)
    weights = [item["weight"] for item in items]
    values = [item["value"] for item in items]
    
    plt.scatter(weights, values, color='blue', label='All items')
    # Mettre en avant les choisis
    chosen_weights = [items[i]["weight"] for i in solution]
    chosen_values = [items[i]["value"] for i in solution]
    plt.scatter(chosen_weights, chosen_values, color='red', s=100, label='Chosen items')
    
    plt.xlabel('Weight')
    plt.ylabel('Value')
    plt.title(f'Knapsack Solution - {name}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
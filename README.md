# Problem Solving Project: Logistics & Transportation (Knapsack)

**Name:** Alexandre Nerdig  
**Topic:** 3A - Logistics and transportation (maximizing package value in a delivery truck under capacity constraints).

## Real-World Scenarios
1. **Delivery Truck Loading:** Selecting the most profitable combination of customer packages for a delivery truck with a strict weight limit.
2. **Container Shipping:** Maximizing the total value of exported goods packed into a shipping container with a maximum load capacity.

## Application Choice & Stack
- **Choice:** Desktop application (command line / simple script output with matplotlib charts).
- **Stack:** Python 3, Matplotlib, Pytest.

## Algorithm Description
- **Name:** Greedy by Value/Weight Ratio (ou Dynamic Programming si tu as choisi ça).
- **Idea:** Tri des objets par ratio valeur/poids décroissant et sélection des meilleurs tant que la capacité le permet.
- **Inputs & Outputs:** Input = JSON avec capacité et liste d'objets. Output = Liste des IDs d'objets choisis.

## How to Run
1. Activer l'environnement virtuel :
   ```bash
   source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows
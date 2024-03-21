"""
I took this code from:
	https://developers.google.com/optimization/pack/knapsack
"""

from ortools.algorithms.python import knapsack_solver

values = [30, 10, 50, 10, 60, 20, 80, 50]
weights = [
    [2, 4, 6, 8, 10, 12, 14, 18],
]
capacities = [30]

solver = knapsack_solver.KnapsackSolver(
    knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
    "KnapsackSolution",
)

solver.init(values, weights, capacities)
computed_value = solver.solve()
packed_items = []
packed_weights = []
total_weight = 0
print("Total value =", computed_value)
for i in range(len(values)):
    if solver.best_solution_contains(i):
        packed_items.append(i)
        packed_weights.append(weights[0][i])
        total_weight += weights[0][i]
print("Total weight:", total_weight)
print("Packed items:", packed_items)
print("Packed_weights:", packed_weights)

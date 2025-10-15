import random
def objective_function(x):
    return -x**2 + 10*x

def hill_climbing(max_iterations=1000, step_size=0.1):
    # Start from a random point
    current_x = random.uniform(0, 10)
    current_value = objective_function(current_x)

    for i in range(max_iterations):
        # Generate a neighboring solution
        neighbor_x = current_x + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor_x)

        # If neighbor is better, move to neighbor
        if neighbor_value > current_value:
            current_x, current_value = neighbor_x, neighbor_value

    return current_x, current_value

# Run the algorithm
solution_x, solution_value = hill_climbing()
print(f"Best solution: x = {solution_x:.4f}, f(x) = {solution_value:.4f}")

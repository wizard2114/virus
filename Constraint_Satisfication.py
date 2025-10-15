#first install using cmd,

#pip install python-constraint


import constraint
# Define the problem
problem = constraint.Problem()
# Regions to color
regions = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
# Available colors
colors = ['Red', 'Green', 'Blue']
# Add variables
for region in regions:
    problem.addVariable(region, colors)
# Define neighbours
neighbours = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW':['SA', 'Q', 'V'],
    'V':  ['SA', 'NSW'],
}
# Add constraints: neighboring regions must have different colors
for region, adjacent in neighbours.items():
    for neighbour in adjacent:
        problem.addConstraint(lambda r, n: r != n, (region, neighbour))

# Get one solution
solution = problem.getSolution()

# Print the result
print("Map Coloring Solution:\n")
for city, color in solution.items():
    print(f"{city:12} {color}")

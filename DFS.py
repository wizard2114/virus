#First run this commands on CMD
#   pip install networkx
#   pip install matplotlib


import networkx as nx
import matplotlib.pyplot as plt

node = input("Enter starting node: ")
visited = set()

def dfs(node, visited, graph):
    """
    Performs Depth First Search traversal on a graph.
    """
    if node not in visited:
        print(node)  # Print the visited node
        visited.add(node)
        # Recursively visit all adjacent nodes
        for i in graph.get(node, []):
            dfs(i, visited, graph)

# Graph defined as an adjacency list (dictionary)
graph = {
    'Devgad': ['Vaibhavadi', 'malvan', 'kankavli'],
    'Vaibhavadi': ['Devgad', 'kankavli'],
    'malvan': ['Devgad', 'kankavli', 'Vengurla', 'Kudal'],
    'kankavli': ['Vaibhavadi', 'Devgad', 'malvan', 'Kudal'],
    'Kudal': ['kankavli', 'malvan', 'Vengurla', 'Sawantwadi'],
    'Vengurla': ['malvan', 'Kudal', 'Sawantwadi'],
    'Sawantwadi': ['Kudal', 'Vengurla', 'Dodamarg'],
    'Dodamarg': ['Sawantwadi']
}

# Start the DFS traversal from the user-provided starting node
print("DFS Traversal:")
dfs(node, visited, graph)

# --- Graph Visualization using networkx ---

# Create a new graph object
G = nx.Graph()

# Add edges to the graph from the dictionary
for graph_node in graph:
    for neighbor in graph[graph_node]:
        G.add_edge(graph_node, neighbor)

# Draw the graph with node labels
nx.draw(G, with_labels=True)

# Display the graph plot
plt.show()

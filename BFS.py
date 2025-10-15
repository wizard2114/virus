#First run this commands on CMD
#   pip install networkx
#   pip install matplotlib


import networkx as nx
import matplotlib.pyplot as plt
import queue

# b. Implement breadth first search algorithm.

# Graph defined as an adjacency list
# Note: 'vaibhavwadi' appears as a neighbor but is not a key,
# so it's a terminal node in this graph representation.
graph = {
    'kudal': ['kankavli', 'vengurla', 'sawantwadi', 'malvan'],
    'kankavli': ['vaibhavwadi', 'devgad', 'malvan', 'kudal'],
    'vengurla': ['malvan', 'kudal', 'sawantwadi'],
    'devgad': ['vaibhavwadi', 'kankavli', 'malvan'],
    'malvan': ['devgad', 'vengurla', 'kankavli', 'kudal'],
    'sawantwadi': ['kudal', 'dodamarg', 'vengurla'],
    'dodamarg': ['sawantwadi']
}

def bfs(start_node):
    """
    Performs Breadth First Search traversal on the graph.
    """
    visited = set()
    q = queue.Queue()

    # Add the starting node to the queue and visited set
    q.put(start_node)
    visited.add(start_node)

    print("BFS Traversal:")
    while not q.empty():
        node = q.get()
        print(node)

        # Get all adjacent vertices of the dequeued vertex
        for adjacent_node in graph.get(node, []):
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                q.put(adjacent_node) # This line was missing in the photo but is essential

# --- Starting the search ---
# The output in the image corresponds to a search starting from 'malvan'
bfs('malvan')

# --- Graph Visualization using networkx ---
G = nx.Graph()

# Add edges to the graph from the dictionary
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

# Draw the graph with node labels and styling
print("\nDisplaying graph...")
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, edge_color='gray')
plt.title("Graph Visualization")
plt.show()

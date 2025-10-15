from queue import Queue
def BreadthFirstSearch(start_node, visited, graph):
    queue = Queue()
    queue.put(start_node)
    traversal_order = []  #to store the BFS order
    while not queue.empty():
        node = queue.get()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.put(neighbor)
    return traversal_order  #return the final BFS order
# Define graph
graph = {
    'Oros': ['Sawantwadi'],
    'Sawantwadi': ['Oros', 'Kudal', 'Vaibhavwadi', 'Dodamarg'],
    'Kudal': ['Sawantwadi', 'Kankavli', 'Vengurla'],
    'Kankavli': ['Kudal', 'Devgad'],
    'Devgad': ['Kankavli', 'Malvan'],
    'Malvan': ['Devgad', 'Vengurla'],
    'Vengurla': ['Malvan', 'Kudal'],
    'Vaibhavwadi': ['Sawantwadi'],
    'Dodamarg': ['Sawantwadi'],
}
# Call BFS
visited = set()
start_node = 'Oros'
bfs_result = BreadthFirstSearch(start_node, visited, graph)
print("\nBFS :", " --> ".join(bfs_result))

def DepthFirstSearch(start_node, visited, graph, path):
    if start_node not in visited:
        path.append(start_node)
        visited.add(start_node)
        for i in graph[start_node]:
            DepthFirstSearch(i, visited, graph, path)

# Define graph
start_node = 'Oros'
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
# Call DFS
visited = set()
path = []
DepthFirstSearch(start_node, visited, graph, path)
print("\nDFS :"," --> ".join(path))

import heapq

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, []))
    cost_so_far = {start: 0}

    while open_list:
        f, current_cost, current_node, path = heapq.heappop(open_list)

        if current_node == goal:
            return path + [current_node]

        for neighbor, cost in graph.get(current_node, {}).items():
            new_cost = current_cost + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                heapq.heappush(open_list, (priority, new_cost, neighbor, path + [current_node]))

    return None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

path = a_star(graph, heuristics, 'A', 'D')
print("Path found:", path)

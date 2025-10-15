from collections import deque

def water_jug_bfs(cap_x,cap_y,target):
    visited=set()
    queue=deque()
    queue.append((0,0,[]))  # (jug1,jug2,path)

    while queue:
        x,y,path=queue.popleft()
        if (x,y) not in visited:
            visited.add((x,y))
            path=path+[(x,y)]
            if x==target or y==target:
                return path

            next_state=[
                (cap_x,y),                      # Fill jug1
                (x,cap_y),                      # Fill jug2
                (0,y),                          # Empty jug1
                (x,0),                          # Empty jug2
                (x-min(x,cap_y-y),y+min(x,cap_y-y)),   # Pour jug1→jug2
                (x+min(y,cap_x-x),y-min(y,cap_x-x))    # Pour jug2→jug1
            ]

            for state in next_state:
                if state not in visited:
                    queue.append((state[0],state[1],path))
    return None

# Example usage
cap_x=4
cap_y=3
target=2

solution=water_jug_bfs(cap_x,cap_y,target)
if solution:
    print("Steps to reach the goal:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

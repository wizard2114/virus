from heapq import heappush, heappop

GOAL = (1,2,3,4,5,6,7,8,0)  # 0 = blank

def h_manhattan(state):
    total = 0
    for i, v in enumerate(state):
        if v == 0: continue
        goal_i = GOAL.index(v)
        r1, c1 = divmod(i, 3)
        r2, c2 = divmod(goal_i, 3)
        total += abs(r1 - r2) + abs(c1 - c2)
    return total

def neighbors(state):
    idx = state.index(0)
    r, c = divmod(idx, 3)
    moves = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nidx = nr*3 + nc
            new_state = list(state)

            new_state[idx], new_state[nidx] = new_state[nidx], new_state[idx]
            moves.append(tuple(new_state))
    return moves

def a_star(start):
    open_heap = []
    heappush(open_heap, (h_manhattan(start), 0, start, []))
    visited = set()
    while open_heap:
        f, g, state, path = heappop(open_heap)
        if state == GOAL:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for nb in neighbors(state):
            if nb not in visited:
                heappush(open_heap, (g+1+h_manhattan(nb), g+1, nb, path+[state]))
    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else " " for x in state[i:i+3]))
    print("--")


# Example run
start = (8,7,6,
         5,4,3,
         2,1,0)

solution = a_star(start)
print(f"Solution found in {len(solution)-1} moves:\n")
for step in solution:
    print_board(step)

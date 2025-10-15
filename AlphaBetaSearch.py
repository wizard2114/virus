import math

# Minimax function with Alpha-Beta Pruning
def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Assume depth = 3 for leaf nodes
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        # Recur for left and right child
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        # Recur for left and right child
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Run alphabeta pruning
print("The optimal value is :", alphabeta(0, 0, True, values, -math.inf, math.inf))

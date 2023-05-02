from queue import PriorityQueue

def multiple_knapsack_bb(capacities, weights, values):
    # capacities: a list of capacities of each knapsack
    # weights: a list of weights of each item
    # values: a list of values of each item
    
    n_knapsacks = len(capacities)
    n_items = len(weights)
    max_value = 0
    
    # Initialize the priority queue with the root node
    # Each node is represented by a tuple (level, value, weight, solution)
    # where level is the index of the current item being considered,
    # value is the total value of the items included so far,
    # weight is the total weight of the items included so far,
    # and solution is a list of length n_knapsacks indicating the
    # number of items placed in each knapsack
    root = (0, 0, 0, [0] * n_knapsacks)
    queue = PriorityQueue()
    queue.put((-root[1], root))
    
    # Branch and bound loop
    while not queue.empty():
        # Get the most promising node from the queue
        _, node = queue.get()
        level, value, weight, solution = node
        
        # If we have reached the last item, update the max value if necessary
        if level == n_items:
            if value > max_value:
                max_value = value
            continue
        
        # Compute the lower bound for the current node
        bound = value
        for i in range(n_knapsacks):
            if weight + weights[level] > capacities[i]:
                # If we can't add the entire item to knapsack i, add a fraction of it
                bound += (capacities[i] - weight) * values[level] / weights[level]
                break
            else:
                bound += values[level]
                weight += weights[level]
        
        # If the lower bound is less than the current max value, prune the node
        if bound < max_value:
            continue
        
        # Explore the two child nodes corresponding to either including or excluding the current item
        solution_included = solution[:]
        solution_included[i] += 1
        node_included = (level+1, value+values[level], weight+weights[level], solution_included)
        queue.put((-node_included[1], node_included))
        
        node_excluded = (level+1, value, weight, solution)
        queue.put((-node_excluded[1], node_excluded))
    
    # Return the optimal solution and its value
    return max_value, solution

from collections import deque

def bfs(graph, initial, goal):
    visited = set()
    queue = deque([initial])
    visited.add(initial)
    path = {initial: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            return path, visited
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                path[neighbor] = current
    return None, visited

# Read input from a text file
with open('in.txt', 'r') as f:
    num_states = int(f.readline())
    graph = {i: set() for i in range(1, num_states + 1)}
    for i in range(1, num_states + 1):
        line = f.readline()
        if line:
            graph[i] = set(map(int, line.strip().split()))
    initial_state = int(f.readline())
    goal_state = int(f.readline())

# Find path from initial state to goal state
path, visited = bfs(graph, initial_state, goal_state)
if path is None:
    if goal_state not in graph.keys():
        print("The goal state is not present in the state space.")
    else:
        print("The goal state is not approachable from the state space.")
else:
    # Print list of all the states traversed
    print("List of all the states traversed:", visited)

    # Print path from initial state to goal state
    current = goal_state
    path_list = []
    while current is not None:
        path_list.append(current)
        current = path[current]
    print("Path from initial state to goal state:", list(reversed(path_list)))

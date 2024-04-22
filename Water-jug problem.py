from collections import deque

# maximum capacities of the containers
capacity_A = 3
capacity_B = 5

# empty at first
initial_state = (0, 0)

# Define the goal
goal = 4

# Define the possible operations
operations = [
    # state[0] is level in container A & vice-versa
    ("Fill A", lambda state: (capacity_A, state[1])),
    ("Fill B", lambda state: (state[0], capacity_B)),
    ("Empty A", lambda state: (0, state[1])),
    ("Empty B", lambda state: (state[0], 0)),
    ("Pour A to B", lambda state: (
        max(0, state[0] - (capacity_B - state[1])),
        min(capacity_B, state[0] + state[1]))
     ),
    ("Pour B to A", lambda state: (
        min(capacity_A, state[0] + state[1]),
        max(0, state[1] - (capacity_A - state[0])))
     )
]


# Perform breadth-first search
def bfs(initial_state, goal):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:  # not empty
        state, path = queue.popleft()
        if state[0] == goal or state[1] == goal:
            return path + [state]
        visited.add(state)  # to avoid revisiting
        # generate new states by applying each operation to the current state
        for operation_name, operation in operations:
            new_state = operation(state)
            if new_state not in visited:
                new_path = path + [(operation_name, new_state)]
                queue.append((new_state, new_path))

    return None


# Main function
def main():
    result = bfs(initial_state, goal)
    if result:
        print("Initial state:", initial_state)
        for operation, state in result:
            print(f"{operation}: {state}")
        print("Desired measure achieved")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()

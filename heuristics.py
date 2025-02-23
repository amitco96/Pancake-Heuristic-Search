def base_heuristic(_pancake_state):
    list_state = _pancake_state.get_list_state()
    for p in range(len(list_state)):
        if list_state[p] != (len(list_state) - p):
            return sum(list_state[p:])
    return 0

def advanced_heuristic(_pancake_state):
    stack = _pancake_state.get_list_state()
    n = len(stack)
    dist = 0
    for i in range(0, n - 1):
        if stack[i] != (stack[i + 1] + 1):
            weight = abs(stack[i + 1] - stack[i])
            dist += weight * (stack[i + 1] + stack[i])
    return dist
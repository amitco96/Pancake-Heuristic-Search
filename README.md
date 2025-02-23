# Pancake Sort Solver

A Python implementation of A* search algorithm that solves the classic Pancake Sorting problem. The project features multiple heuristic functions and efficient state management to find the optimal sequence of flips needed to sort a stack of pancakes.

## 🥞 Problem Description

The Pancake Sorting problem involves sorting a stack of pancakes of different sizes, where the only allowed operation is flipping a prefix of the stack. Each pancake has a different size, and the goal is to sort them in descending order (largest on top).

For example, given the stack: `[2,1,4,5,6,7,3,8,9]`, we want to reach: `[9,8,7,6,5,4,3,2,1]`

## 🚀 Features

- Implementation of A* search algorithm
- Multiple heuristic functions:
  - Base heuristic: Calculates the sum of remaining pancakes when a mismatch is found
  - Advanced heuristic: Uses weighted distances between adjacent pancakes
- Efficient state management using min-heap with dictionary
- Comprehensive path finding and solution tracking

## 📁 Project Structure

```
.
├── main.py           # Main execution file with example problems
├── search.py         # A* search algorithm implementation
├── pancake_state.py  # State representation and neighbor generation
├── search_node.py    # Search node implementation for A*
├── heuristics.py     # Heuristic functions implementation
├── min_heap.py       # Min heap with dictionary implementation
└── test.py          # Test cases for the implementation
```

## 💻 Usage

1. Create a pancake state with a comma-separated string of numbers:
```python
from pancake_state import pancake_state
from heuristics import advanced_heuristic
from search import search

# Initialize a pancake state
initial_state = pancake_state("2,1,4,5,6,7,3,8,9")

# Define goal state
goal_state = "9,8,7,6,5,4,3,2,1"

# Find solution using advanced heuristic
solution_path = search(initial_state, advanced_heuristic, goal_state)
```

## 🧮 Heuristic Functions

### Base Heuristic
```python
def base_heuristic(_pancake_state):
    list_state = _pancake_state.get_list_state()
    for p in range(len(list_state)):
        if list_state[p] != (len(list_state) - p):
            return sum(list_state[p:])
    return 0
```

### Advanced Heuristic
```python
def advanced_heuristic(_pancake_state):
    stack = _pancake_state.get_list_state()
    n = len(stack)
    dist = 0
    for i in range(0, n - 1):
        if stack[i] != (stack[i + 1] + 1):
            weight = abs(stack[i + 1] - stack[i])
            dist += weight * (stack[i + 1] + stack[i])
    return dist
```

## 🔍 Implementation Details

- The `pancake_state` class represents a state in the search space and implements neighbor generation
- `search_node` class maintains node information for A* search (g, h, and f values)
- `min_heap_and_dict` provides efficient open set operations with O(log n) time complexity
- The search implementation supports duplicate detection in both open and closed sets

## 🎯 Example Problems

The implementation includes several test cases:
```python
a = "9,2,5,4,3,6,7,1,8"
b = "2,1,4,5,6,7,3,8,9"
c = "8,6,4,2,7,9,1,3,5"
d = "3,7,8,6,1,5,2,4,9"
e = "4,6,1,5,9,3,2,8,7"
```


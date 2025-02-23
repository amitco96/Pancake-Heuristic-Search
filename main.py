from search import search
from pancake_state import pancake_state
from heuristics import *
import time

if __name__ == '__main__':
    goal_state = "9,8,7,6,5,4,3,2,1"

    a = "9,2,5,4,3,6,7,1,8"
    b = "2,1,4,5,6,7,3,8,9"
    c = "8,6,4,2,7,9,1,3,5"
    d = "3,7,8,6,1,5,2,4,9"
    e = "4,6,1,5,9,3,2,8,7"
    series_list_1 = [a, b, c, d, e]
    start = time.time()
    for item in series_list_1:
        p = pancake_state(item)
        print(search(p, advanced_heuristic, goal_state))
    finish = time.time()
    print(finish - start)

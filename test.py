from pancake_state import pancake_state
from min_heap import min_heap_and_dict
from search_node import search_node
from search import *

open_set = create_open_set()
node1 = search_node(state="A", g=3, h=5)
node2 = search_node(state="B", g=6, h=3)
node3 = search_node(state="C", g=2, h=3)
node4 = search_node(state="D", g=1, h=3)
add_to_open(node1, open_set)
add_to_open(node2, open_set)
add_to_open(node3, open_set)
add_to_open(node4, open_set)






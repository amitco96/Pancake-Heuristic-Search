import heapq


class min_heap_and_dict:
    def __init__(self):
        self.heap = []
        self.dictionary = {}


    def push(self, item):
        heapq.heappush(self.heap, item)
        self.dictionary[item.state] = item

    def pop(self):
        min_value = heapq.heappop(self.heap)
        try:
            del self.dictionary[min_value.state]
            return min_value
        except KeyError:
            raise ValueError("!!!!!!!!")

    def __len__(self):
        return len(self.heap)

    def remove_from_heap(self, value):
        """
        Remove a specific value from a heap.
        """
        try:
            index = self.heap.index(value)
            del self.heap[index]
            heapq.heapify(self.heap)
            del self.dictionary[value.state]
        except ValueError:
            pass



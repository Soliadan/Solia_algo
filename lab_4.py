class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"({self.value}, priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        max_node = self.heap[0]
        last_node = self.heap.pop()
        if self.heap:
            self.heap[0] = last_node
            self._heapify_down(0)
        return max_node

    def peek(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[largest] < self.heap[left]:
            largest = left
        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)

    def __repr__(self):
        return str(self.heap)


if __name__ == "__main__":

    pq = PriorityQueue()
    pq.insert("Task 1", 3)
    pq.insert("Task 2", 5)
    pq.insert("Task 3", 1)
    pq.insert("Task 4", 4)

    print("Queue:", pq)
    print("High priority:", pq.peek())
    print("Deletion:", pq.extract_max())
    print("Updated queue:", pq)

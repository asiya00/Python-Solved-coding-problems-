class Priority_Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.pointer = -1;

    def left_child(self, index):
        return 2*index + 1

    def right_child(self, index):
        return 2*index + 2

    def parent(self, index):
        return (index-1)//2

    def minheapify(self, index, heapsize):
        left = self.left_child(index)
        right = self.right_child(index)
        largest = index
        if left <= heapsize and self.arr[left] < self.arr[largest]:
            largest = left
        if right <= heapsize and self.arr[right] < self.arr[largest]:
            largest = right

        if largest != index:
            self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
            self.minheapify(largest, heapsize)

    def build_min_heap_tree(self, heapsize):
        for i in range(heapsize//2, -1, -1):
            self.minheapify(i, heapsize)

    def heap_minimum_value(self):
        return self.arr[0]

    def heap_decrease_value(self, index, key):
        if key > self.arr[index] and index > self.pointer:
            return "Key Value is greater than the original Value or index not found"
        self.arr[index] = key
        while index > 0 and self.arr[self.parent(index)] > self.arr[index]:
            self.arr[index], self.arr[self.parent(index)] = self.arr[self.parent(index)], self.arr[index]
            index = self.parent(index)

    def insert_queue(self, data):
        if self.pointer != self.size - 1:
            self.pointer += 1
            self.arr[self.pointer] = float("inf")
            self.heap_decrease_value(self.pointer, data)
        else:
            return "Queue is Full"

    # def insert_queue(self,data):
    #     if self.pointer != self.size - 1:
    #         self.pointer += 1
    #         self.arr[self.pointer] = data
    #         self.build_min_heap_tree(self.pointer)
    #     else:
    #         return "Queue is Full"

    def remove_queue(self):
        if self.pointer == -1:
            return "Queue is empty"
        else:
            self.arr[0], self.arr[self.pointer] = self.arr[self.pointer], self.arr[0]
            removed = self.arr[self.pointer]
            self.pointer = self.pointer - 1
            self.minheapify(0, self.pointer)

    def remove_element(self, data):
        if self.pointer == -1:
            return "Queue is empty"
        else:
            try:
                i = self.arr.index(data)
                self.arr[i], self.arr[self.pointer] = self.arr[self.pointer], self.arr[i]
                self.pointer = self.pointer - 1
                self.minheapify(i, self.pointer)
            except ValueError:
                print("Element not found")

    def display(self):
        return self.arr[:self.pointer+1]


pqueue = Priority_Queue(10)
pqueue.insert_queue(16)
pqueue.insert_queue(4)
pqueue.insert_queue(10)
pqueue.insert_queue(14)
pqueue.insert_queue(7)
pqueue.insert_queue(9)
pqueue.insert_queue(3)
pqueue.insert_queue(2)
pqueue.insert_queue(8)
pqueue.insert_queue(1)
print(pqueue.display())
pqueue.remove_queue()
print(pqueue.display())
print(pqueue.heap_minimum_value())
# pqueue.remove_element(11)
print(pqueue.display())

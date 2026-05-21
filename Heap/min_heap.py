class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        current=len(self.heap)-1
        while current >0 and self.heap[self._parent(current)]>self.heap[current]:
            self._swap(self._parent(current),current)
            current=self._parent(current)

 
 
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)

print(myheap.heap)  

myheap.insert(4)

print(myheap.heap)  

myheap.insert(2)

print(myheap.heap)  



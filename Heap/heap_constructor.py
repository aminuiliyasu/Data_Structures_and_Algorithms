class MaxHeap:
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
        index=len(self.heap)-1
        while index>0 and self.heap[index]>self.heap[self._parent(index)]:
            
            self._swap(index,self._parent(index))
            index=self._parent(index)
    
    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return root
    
    def _sink_down(self,index):
        max_index=index
        while True:
            left_index=self._left_child(index)
            right_index=self._right_child(index)
            if left_index<len(self.heap) and self.heap[left_index]>self.heap[max_index]:
                max_index=left_index
            if right_index<len(self.heap) and  self.heap[right_index]>self.heap[max_index]:
                max_index=right_index
            if max_index!=index:
                self._swap(max_index,index)
                index=max_index
            else:
                return
    
    
myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)  


myheap.insert(100)

print(myheap.heap)  


myheap.insert(75)

print(myheap.heap)


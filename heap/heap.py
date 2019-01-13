class heap(object):
    """this class implements a max heap and provides the following functions:
    buildheap, maxheapify, heapsort, extract-max
    """
    def __init__(self, arr = []):
        self.heap = arr
        self.size = len(self.heap)

    def maxheapify(self,i):
        left = 2*i +1
        right = 2*i+2
        if left < self.size and self.heap[left] > self.heap[i]:
            largest = left
        else:
            largest = i
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp
            self.maxheapify(largest)

    def buildheap(self):
        for i in range(self.size//2 -1, -1,-1):
            self.maxheapify(i)

    def heapsort(self):
        self.buildheap()
        for i in range(len(self.heap)-1,0,-1):
            temp = self.heap[i]
            self.heap[i] = self.heap[0]
            self.heap[0] = temp
            self.size -= 1
            self.maxheapify(0)

    def printheap(self):
        print(self.heap)

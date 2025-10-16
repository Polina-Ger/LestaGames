class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=0
        self.previous=0
class cyclic_buffer_doubleList:
    def __init__(self, capacity):
        if capacity<1: raise ValueError("Capacity must be more than 1!")
        self.capacity=capacity
        self.first=0
        self.last=0
        self.size=0
        self.create_nodes()

    def create_nodes(self):
        firstNode=Node()
        prev=firstNode
        for i in range(self.capacity-1):
            node=Node()
            prev.next=node
            node.previous=prev
            prev=node
        firstNode.previous=prev
        prev.next=firstNode
        self.first=firstNode
        self.last=firstNode


    def is_full(self):
        return self.size==self.capacity
    def is_empty(self):
        return self.size==0

    def put(self, value):
        self.last.value=value
        self.last=self.last.next
        if self.is_full():
            self.first=self.first.next
        else:self.size+=1
    
    def get(self):
        if self.is_empty():
            print("List is empty!")
            return
        taken_value=self.first.value
        self.first=self.first.next
        self.size-=1
        return taken_value

    def print_arr(self):
        arr = [None]*self.capacity
        for i in range(self.capacity):
            arr[i]=self.first.value
            self.first=self.first.next
        print(arr)

arr1=cyclic_buffer_doubleList(4)
arr1.put(2)
arr1.put(3)
arr1.put(4)
arr1.put(5)
arr1.print_arr()
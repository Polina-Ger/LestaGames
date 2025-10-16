class cyclic_buffer:
    def __init__(self, capacity):
        if capacity<1: raise ValueError("Capacity must be more than 1!")
        self.arr=[None]*capacity
        self.capacity=capacity
        self.first=0
        self.last=0
        self.size=0

    def is_full(self):
        return self.size==self.capacity
    def is_empty(self):
        return self.size==0

    def put(self, value):
        self.arr[self.last]=value
        self.last += 1
        if self.last == self.capacity:
            self.last = 0
        if self.is_full():
            self.first += 1
            if self.first == self.capacity:
                self.first = 0
        else:self.size+=1
    
    def get(self):
        if self.is_empty():
            print("Array is empty!")
            return
        taken_value=self.arr[self.first]
        self.first += 1
        if self.first == self.capacity:
            self.first = 0
        self.size-=1
        return taken_value

    def print_arr(self):
        arr = [None]*self.capacity
        for i in range(self.capacity):
            arr[i]=self.arr[self.first]
            self.first += 1
            if self.first == self.capacity:
                self.first = 0
        print(arr)

arr1=cyclic_buffer(4)
arr1.put(2)
arr1.put(3)
arr1.put(4)
arr1.put(5)
arr1.put(6)
arr1.print_arr()
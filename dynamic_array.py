# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Justin McCune
import numpy as np 



class DynamicArray:

    def __init__(self):
        self.capacity = 10
        self.n = 0
        self.next_index = 0
        self.arr = [0,0,0,0,0,0,0,0,0,0]
        self.data = np.empty([10,1], dtype='O')

    def is_empty(self):
        if self.n == 0:
            return True
        else: 
            return False
    
    def __len__(self):
        return self.n

    def __setitem__(self, index, item):
        self.arr[index] = item
    
    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        if index > self.n-1:
            raise IndexError
        return self.arr[index]
    
    def append(self, item):
        len(self.arr)
        if self.n == self.capacity:
            self.rebuildArray()
        self.arr[self.n] = item
        self.data[self.n] = item
        #increment
        self.n = self.n+1
        self.next_index = self.next_index+1
    
    def clear(self):
        self.arr = [0,0,0,0,0,0,0,0,0,0]
        self.data = np.empty([10,1], dtype='O')
        self.next_index = 0
        self.n = 0
    
    def pop(self):
        if(self.n == 0):
            raise IndexError
        x = self.arr[self.n-1]
        self.arr[self.n-1] = 0
        self.n = self.n -1
        self.next_index = self.next_index -1
        return x
    
    def delete(self, index):
        if index >= self.n:
            raise IndexError
        if index < 0:
            raise IndexError
        numShifts = self.n - index
        while numShifts > index:
            self.arr[index] = self.arr[index+1]            
            index = index+1
        #decrement
        self.n = self.n -1
        self.next_index = self.next_index -1
    
    def insert(self, index, item):
        if self.n == self.capacity:
            self.rebuildArray()
        if index > self.n:
            raise IndexError
        if index == self.n:
            self.arr[self.n] = item
            self.data[self.n] = item
        numShifts = self.n - index
        idx = self.n-1
        while idx > index-1:
            self.arr[idx+1] = self.arr[idx]
            idx = idx-1
        self.arr[index] = item
        #increment
        self.n = self.n+1
        self.next_index = self.next_index+1

    def is_full(self):
        if len(self) == self.capacity:
            return True
    
    def rebuildArray(self):
        oldCap = self.capacity
        self.capacity = oldCap*2
        oldArray = self.arr
        #self.arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.arr = [0]*self.capacity
        self.arr[0:oldCap] = oldArray[0:oldCap]
        self.data = np.empty([self.capacity,1], dtype='O')    
        
    def max(self):
        if self.n == 0:
            return None
        highest = 0
        for x in range(len(self.arr)):
            if self.arr[x] > highest:
                highest = self.arr[x]
        return highest
    
    def min(self):
        if self.n == 0:
            return None
        lowest = self.arr[0]
        for x in range(len(self.arr)):
            if self.arr[x] < lowest:
                lowest = self.arr[x]
        return lowest
    
    def sum(self):
        if self.n == 0:
            return None
        sum = 0
        for x in range(len(self.arr)):
            sum = sum+int(self.arr[x])
        return sum
    
    def linear_search(self, des):
        for x in range(len(self.arr)):
            if self.arr[x] == des:
                return x

    def binary_search(self, des):
        desRange = self.arr
        # split = int(len(desRange)/2)
        # print("one    ",self.arr[split])
        # desRange = desRange[split:len(desRange)]
        # print("two    ", self.arr[int(len(desRange)/2)])    
        
        size = self.n+1    
        return self.myBinarySearch(des, desRange, size)
            

    def myBinarySearch(self, des, desRange, size):
        split = int(size/2)
        
        if len(desRange)<8:
          #  print(desRange)
          #  print(split)
          #  print(size)
            if desRange[0] == des:
                return 0
            if desRange[1] == des:
                return 1
        #if len(desRange)<3
        if desRange[split] == des:
            return split
        if des > desRange[split]:
            desRange = desRange[split:size]
        else:
            desRange = desRange[0:split]
        size = size-split
        self.myBinarySearch(des, desRange, size)
        



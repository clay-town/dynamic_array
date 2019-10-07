# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Justin McCune
import numpy as np 



class DynamicArray:

    capacity = 10
    n = 0
    next_index = 0
    arr = [0,0,0,0,0,0,0,0,0,0]
    data = np.empty([10,1], dtype='O')
    pass
    
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
    
    def append(self, int):
        len(self.arr)
        self.arr[self.n] = int
        self.data[self.n] = int
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
        x = 0
        numShifts = self.n - index
        while numShifts > x:
            self.arr[x] = self.arr[x+1]
            #self.data[x] = self.data[x+1]
            x = x+1
        #decrement
        self.n = self.n -1
        self.next_index = self.next_index -1
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
        return True
    def __len__(self):
        return self.n 
    def __setitem__(self, index, item):
        self.arr[index] = item
    def __getitem__(self, index):
        return self.arr[index]
    def append(self, int):
        len(self.arr)
        self.arr[self.n] = int
        self.data[self.n] = int
        self.n = self.n+1
        self.next_index = self.next_index+1
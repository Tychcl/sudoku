import numpy as np
from itertools import product
from random import shuffle

class sudoku:
    def __init__(self, n=3):
        self.n = n
        self.cells = n**2
        self.chars = np.array(range(1, self.cells+1))
        self.field = np.zeros((self.cells, self.cells), dtype=np.int8)
        self.run()

    def get_bounds(self, row, col):
        start_row = (row // self.n) * self.n
        start_col = (col // self.n) * self.n
        return start_row, start_col

    def get_chunk(self, row, col):
        row, col = self.get_bounds(row, col)
        return set(self.field[row : row + self.n, col : col + self.n].flatten())
    
    def get_set(self, row, col):
        if self.field[row, col] != 0:
           return set()
        
        used_in_row = set(self.field[row, :])
        used_in_col = set(self.field[:, col])
        used_in_block = self.get_chunk(row, col)
        
        return set(self.chars) - (used_in_row | used_in_col | used_in_block)
    
    def find_empty(self):
        for i, j in product(range(self.cells), range(self.cells)):
            if self.field[i, j] == 0:
                return i, j
        return None
    
    def fill_diag(self):
        for i in range(0, self.cells, self.n):
            sr, sc = self.get_bounds(i,i)
            shuffle(self.chars)
            self.field[sr : sr + self.n, sc : sc + self.n] = self.chars.reshape(self.n, self.n)

    def fill_all(self, row, col):
        empty = self.find_empty()
        if empty is None:
            return True
        
        row, col = empty
        available_numbers = list(self.get_set(row, col))
        shuffle(available_numbers)
        for num in available_numbers:
            self.field[row, col] = num
            if self.fill_all(row, col):
                return True
            self.field[row, col] = 0
        
        return False
        
    def run(self):
        self.fill_diag()
        print(self.fill_all(0, 0))

s = sudoku()
print(s.field)
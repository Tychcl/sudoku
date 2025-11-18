import numpy as np
from itertools import chain
import random 
n = 3
cells = n ** 2
chars = list(range(1,cells+1))
#random.shuffle(chars)
#print(set(chars) - {1,2,3})
field = np.zeros((cells, cells), dtype=np.int8)

def bounds(element_index, chunk_size=n):
    chunk_number = element_index // chunk_size
    start_index = chunk_number * chunk_size
    end_index = start_index + chunk_size
    return start_index, end_index
#field[0:3,0:3] = [chars[0:3], chars[3:6], chars[6:9]]
#print(field)
try:
    for y in range(cells):
        row = set(field[y,:])
        for x in range(cells):
            column = set(field[:,x])
            xs, xe = bounds(x)
            ys, ye = bounds(y)
            chunk = set(chain(*field[ys:ye, xs:xe]))
            print(f"{row | column | chunk}")
            field[y,x] = random.choice(list(chars - (row | column | chunk)))
            row.add(field[y,x])
            chunk.add(field[y,x])
except:
    print(field)

        
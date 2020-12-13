# Inspired by
# https://ncase.me/polygons/

import random
import colorama
import numpy

def coinflip():
    return True if random.randint(0,1) else False

def smallestDivisor(n): 
    if not n % 2:
        return 2 
    i = 3
    while i**2 <= n: 
        if (n % i == 0): 
            return i 
        i += 2 
    return n

class Shape:
    count = 0
    def __init__(self, char, happiness_condition=lambda x: x >= 1/3):
        self.id = Shape.count + 1
        Shape.count += 1
        self._char = char
        self._happiness_cond = happiness_condition
    
    def __str__(self):
        return self._char    
    
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        
        return self.id == other.id

    @property
    def pos(self):
        for y in range(grid.length):
            for x in range(grid.length):
                if grid.array[y][x] == self:
                    return x, y

    @property
    def neighbors(self):
        x, y = self.pos
        positions = [
            (x-1,y-1),(x,y-1),(x+1,y-1),
            (x-1,y),(x,y),(x+1,y),
            (x-1,y+1),(x,y+1),(x+1,y+1),
        ]
        neighbors = []
        for posx, posy in positions:
            try:
                shape = grid.array[posy][posx]
                neighbors.append(shape)
            except IndexError:
                pass
        return neighbors

    def similar(self, other):
        return type(self) == type(other)

    @property
    def is_happy(self):
        neighbors = self.neighbors
        total = len(neighbors)
        same = [shape for shape in neighbors if self.similar(shape)]
        similar = len(same)
        return self._happiness_cond(similar/total)
    
    def move(self):
        randx, randy = random.choice(grid.empty_spaces)
        x, y = self.pos
        grid.array[y][x] = None
        grid.array[randy][randx] = self
        print(colorama.ansi.clear_screen(), flush=True)
        grid.print()
    

class Triangle(Shape):
    def __init__(self, cond):
        super().__init__('▼', cond)

class Square(Shape):
    def __init__(self, cond):
        super().__init__('□', cond)
    
class Grid:
    def __init__(self, length, happy):
        self.array = [[None] *  length for _ in range(length)]
        self.length = length
        self.happy = happy
        self.generate_board()

    def generate_board(self):
        for y in range(self.length):
            for x in range(self.length):
                if coinflip():
                    self.array[y][x] = Triangle(self.happy)
                else:
                    self.array[y][x] = Square(self.happy)
                if coinflip() and coinflip() and coinflip():
                    self.array[y][x] = None
    
    def print(self):
        string = '\n'.join([' '.join([str(x) if x is not None else ' ' for x in y]) for y in self.array])
        print(string)
        print('Segregated: ', grid.segregation_percentage, '%', sep='')

    @property
    def empty_spaces(self):
        spaces = []
        for y in range(self.length):
            for x in range(self.length):
                if self.array[y][x] is None:
                    spaces.append((x, y))
        return spaces
    
    @property
    def not_happy_shapes(self):
        for y in self.array:
            for x in y:
                if x is not None:
                    if not x.is_happy:
                        yield x

    def city_blocks(self, rows, cols):
        if self.length  % rows != 0 or self.length % cols != 0:
            raise IndexError('Invalid block length. Rows or cols not divide length cleanly.')
        
        arr = numpy.array(self.array)
        h, w = arr.shape
        return arr \
            .reshape(h//rows, rows, -1, cols) \
            .swapaxes(1,2) \
            .reshape(-1, rows, cols)

    def pop_count(self, block):
        s, t = 0, 0
        for y in block:
            for shape in y:
                if type(shape).__name__ == 'Square':
                    s += 1
                elif type(shape).__name__ == 'Triangle':
                    t += 1
        return s, t

    @property
    def segregation_percentage(self):
        # See https://en.wikipedia.org/wiki/Index_of_dissimilarity
        n = smallestDivisor(self.length)
        blocks = [self.pop_count(block) for block in self.city_blocks(n, n)]
        
        s, t = zip(*blocks)
        S, T = sum(s), sum(t)
        s = [i/S for i in s]
        t = [i/T for i in t]
        dif = [i-j for i, j in zip(s,t)]
        abs_sum = sum([abs(i) for i in dif])
        return int(str(abs_sum/2)[2:4])


import time

# Modify this to change when shapes want to move.
# You can use inequalities
# x: the percentage of neighbors like a shape
happiness_condition = 'x >= 1/3'


def happy(x): return eval(happiness_condition)

grid = Grid(20, happy)

while True:
    try:
        shape = random.choice(list(grid.not_happy_shapes))
        shape.move()
        time.sleep(0.1)
    except IndexError:
        break

print('\nWe have reached 100% happiness')
print(
    '\nWhere Shapes want to move if this is not True:', 
    happiness_condition
        .replace('x', '<like-neighbor-percentage>'), 
    sep='\n'
)
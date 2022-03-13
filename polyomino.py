from functools import partial
from itertools import repeat, starmap

# rotate n*90
def rotation(self, n, x):
    n %= 4
    return {
        n == 0: (x[0], x[1]), # 0
        n == 1: (-x[1], x[0]), # Pi/2
        n == 2: (-x[0], -x[1]), # Pi
        n == 3: (x[1], -x[0]) # 3*Pi/2
        }[False]


def star(f):
    return lambda args: f(*args)

get_x = lambda x: (x[0]) # getX = lambda x, y: (x)
get_y = lambda y: (y[1]) # getY = lambda x, y: (y)

dot = ((0, 0),)

class Polyomino:

    # Polyomino contains its coordinates in the format [(0, 1), (0,2)...]
    def __init__(self, coords):
        self.coords = coords

    def __repr__(self):
        return ''.join(str(x) for x in self.coords)

    def clone(self):
        return Polyomino(self.coords)

    def normalize(self):
        smallestX = min(list(map(get_x, self.coords)))
        smallestY = min(list(map(get_y, self.coords)))
        return self.translate(-smallestX, -smallestY);

    def translate(self, dx, dy):
        t = lambda x: (x[0] + dx, x[1] + dy)
        return Polyomino(list(map(t, self.coords)))

    def rotate(self, n):
        return Polyomino(list(map(partial(rotation, self.coords, n), self.coords)))

    def get_max_x(self):
        return max(list(map(get_x, self.coords)))

    def get_max_y(self):
        return max(list(map(get_y, self.coords)))

    def contain_coords(self, c):
        return set(c.coords).issubset(self.coords)

    

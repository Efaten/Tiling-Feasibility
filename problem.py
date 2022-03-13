from math import sqrt
from polyomino import *


class Problem:

    def __init__(self, pieces, region):
        # All polyominoes
        self.pieces = pieces
        # Table (polyomino as well)
        self.region = region
        self.height = region.get_max_y()
        self.width = region.get_max_x()
        
    def fits(self, piece):
        if piece.get_max_x() < self.width & piece.get_max_y() < self.height:
            return self.region.contain_coords(piece)
        return False

    # All possible placement options, including rotation 
    def generate_configurations(self, piece):
        for rota in range(4):
            for dx in range(self.width):
                for dy in range(self.height):
                    config = piece.rotate(rota)
                    config = config.normalize()
                    config = config.translate(dx, dy)

                    if self.fits(config):
                        yield config

    # Construct a matrix representation of the exact coverage problem
    def dlx(self):
        matrix = []
        configs = []
        row_size = len(self.pieces) + len(self.region.coords)
        for p_index, p in enumerate(self.pieces):
            # screwed up a little, identical configs are created 
            configs.append(list(self.generate_configurations(p)))
            for c in configs:
                row = [0 for i in range(row_size)]
                row[p_index] = 1
                for coord in c:
                    for tmp in coord.coords:
                        index = self.region.coords.index(tmp)
                        row[len(self.pieces) + index] = 1
            
                matrix.append(row)
        # TODO: should have created a dictionary right away 
        return matrix


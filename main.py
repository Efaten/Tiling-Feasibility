from polyomino import Polyomino, dot
from util import parse
from problem import *
from solver import *


def main():
    while True:
        pols = parse()
        region = Polyomino(pols[0])
        pieces = []
        count = 0
        for p in pols[1:]:
            for el in p:
                count += len(el) + 1
                pieces.append(Polyomino(el))
        count -= len(pieces) + 1

        # since we are expanding the problem to an exact cover,
        # it is necessary to supplement the polyomino
        # of a square of dimensions 1x1 (dot)
        while count <= len(region.coords):
            pieces.append(Polyomino(dot))
            count += 1
        
        prob = Problem(pieces, region)
        matrix = prob.dlx()

        # the need to get rid of duplicates in the matrix 
        new_list = []
        url_set = []
        # TODO: get rid of this cycle
        for item in matrix:
            if item not in url_set:
                url_set.append(item)
                new_list.append(item)

        matrix_dict = matrix_to_dict(new_list)
        seconddict = create_second_dict(matrix_dict)
        nn = list(solve(matrix_dict, seconddict))
        # Check if solution covers all possible dictionary keys 
        for n in nn:
            for x in n:
                del(seconddict[x])

        if seconddict:
            print(True)
        else: 
            print(False)

if __name__ == '__main__':
    main()

# TODO: Check for possible answers for an existing tiling smaller than the size of the table (not exact cover)

# TODO: z3 theorem solver should work fine
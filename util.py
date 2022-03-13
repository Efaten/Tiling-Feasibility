from ast import literal_eval as make_tuple

# parses 3 line of input into coords
def parse():
    #print("Enter table size (n, m):\n > ", end='')
    # Table with x to y size 
    region = input()
    #print("Enter rectangular polyomino [((n, m), c)...]:\n >", end='')
    # Rectangular polyminoes ((n, m), c), where (n, m) - size, c - number of figures
    squares = input()
    #print("Enter L-minoes [((n, m), c)...]:\n >", end='')
    # L-minoes ((n, m), c), where n - number of squares horizontally; m - number of vertical squares;
    # c - number of figures
    lmino = input()

    r = make_tuple(region)
    s = make_tuple(squares)
    l = make_tuple(lmino) 

    result = []
    # Generate region coords
    result.append(region_coords(r))

    # Generate rectangular polyomino 
    # if len(s) > 1:
    #     for smt in s:
    #         result.append(squares_coords(smt))
    # else: 
    #     result.append(squares_coords(s))
    for item in s:
        result.append(squares_coords(item))

    # Generate L-mino 
    if (type(l[1]) == tuple):
        for smt in l:
            result.append(lmino_coords(smt))
    else: result.append(lmino_coords(l))
    # TODO: foolproof 
    return result

def region_coords(region):
    result = []
    for x in range(region[0]):
        for y in range(region[1]):
            result.append((x, y))

    return result

def squares_coords(squares):
    sqr = []
    result = []
    cycle = squares[0]
    for x in range(squares[1]):
        for y in range(cycle[0]):
            for z in range(cycle[1]):
                sqr.append((y, z))
        result.append(tuple(sqr))
        sqr = []
    return result

def lmino_coords(lmino):
    result = []
    lmin = []
    cycle = lmino[0]
    for x in range(lmino[1]):
        for y in range(cycle[0]):
            lmin.append((y, 0))
        for y in range(cycle[1]):
            lmin.append((0, y))
        result.append(tuple(set(lmin)))
        lmin = []
    return result


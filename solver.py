# The main idea is to use dictionnaries instead of doubly-linked lists to represent the matrix.
# So the input:
"""
X' = {1, 2, 3, 4, 5, 6, 7}   => X = {                     Y = Y'
Y' = {                          1: {'A', 'B'},
    'A': [1, 4, 7],             2: {'E', 'F'},
    'B': [1, 4],                3: {'D', 'E'},
    'C': [4, 5, 7],             4: {'A', 'B', 'C'},
    'D': [3, 5, 6],             5: {'C', 'D'},
    'E': [2, 3, 6, 7],          6: {'D', 'E'},
    'F': [2, 7]}                7: {'A', 'C', 'E', 'F'}}
"""
# this can also be used for bipartite graph representation 

# Knuth's Algorithm X with dlx
def solve(X, Y, solution=[]):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()

def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k] = set(X[k])
                    X[k].add(i)

# Creates X from matrix
def matrix_to_dict(matrix):
    newmatrix = []
    for tmp, r in enumerate(matrix):
        newmatrix.append([])
        for idx, stat in enumerate(r):
            if stat == 1: newmatrix[tmp].append(chr(97+idx))
        r = r.remove(0)

    res = {idx: val for idx, val in enumerate(newmatrix, start = 1)}
    return res

# Creates Y from first dict
def create_second_dict(d):
    s = set()
    for key, val in d.items():
        for item in val:
            s.add(item)

    answer = dict((el, set()) for el in s)
    for key, val in d.items():
        for item in val:
            if item in answer.keys(): 
                answer[item].add(key)

    for k, v in answer.items():
        answer[k] = list(v)
    return answer



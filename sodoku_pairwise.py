# sodoku.py - Representation of a sodoku solver using alldifferent
# Python 3 code. Full documentation at http://artint.info/code/python/code.pdf

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2015.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US.


from cspProblem import Constraint, CSP

digits = [1,2,3,4,5,6,7,8,9]

def pairwise(a,b):
    """Returns True if all of the arguments are different.
    """
    return a != b
    
def create_constraints():

    return [Constraint([(x,y),(a,b)], pairwise) for y in range(9) \
    for x in range(9) for b in range(9) for a in range(9) \
    if (not (x == a and y == b)) and (x == a or y == b or \
    (x // 3 == a // 3 and y // 3 == b // 3))]

def sodoku_CSP(eg):
    """returns a CSP where the non-zero values in eg have been assigned.
    eg[y][x] gives the value in column y, row x, or 0 if it is unknown
    """

    constraints = create_constraints();

    return CSP(
        {(x,y):(digits if eg[y][x]==0 else [eg[y][x]])
            for x in range(9) for y in range(9)},
        constraints)

easy = [[7,3,0,0,0,0,6,9,0],
        [0,0,0,0,0,0,0,2,5],
        [0,0,0,3,0,5,0,8,4],
        [5,9,0,0,2,6,0,0,0],
        [0,7,8,5,0,3,9,4,0],
        [0,0,0,7,9,0,0,3,6],
        [3,2,0,9,0,1,0,0,0],
        [1,5,0,0,0,0,0,0,0],
        [0,6,4,0,0,0,0,5,9]]

goldenNuggetEg = [
    [0,0,0,0,0,0,0,3,9],
    [0,0,0,0,0,1,0,0,5],
    [0,0,3,0,5,0,8,0,0],
    [0,0,8,0,9,0,0,0,6],
    [0,7,0,0,0,2,0,0,0],
    [1,0,0,4,0,0,0,0,0],
    [0,0,9,0,8,0,0,5,0],
    [0,2,0,0,0,0,6,0,0],
    [4,0,0,7,0,0,0,0,0]]
    
egCSP = sodoku_CSP(easy)
#egCSP = sodoku_CSP(goldenNuggetEg)

def print_sodoku(sodoku_domains):
    """prints the domains of a sodoku
    """
    for y in range(9):
        print(*[sodoku_domains[(x,y)] for x in range(9)],sep=",")
print("printing egCSP domains:")
print_sodoku(egCSP.domains)
print("finished printing egCSP domains")
from cspSearch import Search_from_CSP
from cspConsistency import Search_with_AC_from_CSP, CSP_with_restriction
from searchDepthFirst import Depth_first_search

ac_csp = CSP_with_restriction(egCSP)
# solver = Depth_first_search(Search_with_AC_from_CSP(egCSP))
# print(solver.search())

# To time the calls.
import timeit
print(timeit.timeit("print(Depth_first_search(Search_with_AC_from_CSP(egCSP)).search())",setup="from __main__ import Depth_first_search,Search_with_AC_from_CSP,egCSP",number=1))


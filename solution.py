import itertools
import functools

def solution(xs):
    max = 0
    for i in range(len(xs)):
        cs = list(itertools.combinations(xs,i))
        for c in cs:
            m = functools.reduce(lambda x, y: x * y, c, 1)
            if m > max: max = m


    return str(max)
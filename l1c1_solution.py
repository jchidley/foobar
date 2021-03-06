# https://foobar.withgoogle.com
# Level 1, Challenge 1
# %%
import itertools


# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/


def eratosthenes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]:  # move each witness to its next multiple
                D.setdefault(p+q, []).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1


# %%
max_size = 10005
list_of_primes = ""
e = eratosthenes()
while len(list_of_primes) < max_size:
    list_of_primes += str(next(e))

# %%


def solution(n):
    return list_of_primes[n:n+5]

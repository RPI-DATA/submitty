"""
Sample output to test doctest
"""

import math

def findmax(L):

	"""
    >>> L1 = [ 1, 4, 5, 10 ]
    >>> findmax(L1)
    10
    >>> L2 = [ 1, 3, 9, 33, 81 ]  
    >>> findmax(L2)
    81
    """

	return max(L)

def findmin(L):

	"""
    >>> L3 = [ 1, 4, 5, 10 ]
    >>> findmin(L3)
    1
    >>> L4 = [ 9, 10, 22, 44, 55 ]  
    >>> findmin(L4)
    9
    """

	return min(L)


if __name__ == "__main__":
	pass

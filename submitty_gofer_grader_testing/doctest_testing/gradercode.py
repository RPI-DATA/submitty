import doctest
import testcode

"""
Doctest works with the testcode. Now use the same methodology for the Gofer
Grader configuration.
"""

if __name__ == "__main__":
	doctest.testmod(testcode, verbose=True)
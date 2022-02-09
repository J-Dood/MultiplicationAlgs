# By: Jordan Dood and Christine Johnson
# 2/6/2022
# This code takes two polynomials as vectors and multiplies them using several
# different algorithms and returns a polynomial as a vector.
#
# This file runs the naive O(n^2) algorithm

import Polynomial

def naive(poly1, poly2):
    """
    :argument poly1: List
    :argument poly2: List
    :returns: List
    """
    # Code to match the lengths, if needed
    if len(poly1) != len(poly2):
        if len(poly1) > len(poly2):
            poly2 = extend(poly2, len(poly1))
        else:
            poly1 = extend(poly1, len(poly2))

    # Create and populate result list with 0
    result = []
    for i in range(len(poly2)*2 - 1):
        result.append(0)

    # Double loop multiplication of terms
    for i in range(len(poly1)):
        term1 = poly1[i]
        for j in range(len(poly2)):
            result[i+j] += poly2[j]*term1
    return result


# Function to extend a polynomial
def extend(poly, number):
    for i in range(number-len(poly)):
        poly.append(0)
    return poly


# Driver for testing
if __name__ == '__main__':
    test1 = [3, -4, 5]  # 5X^2 - 4X + 3
    test2 = [-8, 10]    # 10X -8
    test3 = [0]         # 0x
    print(naive(test1, test2))  # 50X^3 - 80X^2 + 62X -24 --> [-24, 62, -80, 50, 0]
    print(naive(test1, test3))  # [0, 0, 0, 0, 0]

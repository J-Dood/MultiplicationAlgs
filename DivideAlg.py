# By: Jordan Dood and Christine Johnson
# 2/6/2022
# This code takes two polynomials as vectors and multiplies them using several
# different algorithms and returns a polynomial as a vector.
#
# This file runs the O(n^1.59) divide and conquer algorithm


def divide(polyA, polyB):
    """
    :argument polyA: List
    :argument polyB: List
    :returns: List
    """
    polyA, polyB = adjust(polyA, polyB)
    # Create and populate result list with 0
    result = []
    for i in range(len(polyB)*2 - 1):
        result.append(0)

    # Base Case
    if len(polyA) == 1:
        return [polyA[0]*polyB[0]]
    # Recursive Case
    else:
        # Make Polynomials even lengths
        if len(polyA)%2 != 0:
            polyA = extend(polyA, 1)
            polyB = extend(polyB, 1)

        # Split the polynomial
        middle = len(polyA)//2
        polyA1, polyA2 = split(polyA, middle)
        polyB1, polyB2 = split(polyB, middle)

        # First Term (X^n)*A(X)*B(X)
        term = polyA[-1] * polyB[-1]
        result[-1] += term

        # TODO
        # Need to shift things, that is one issue

        # Middle Terms, with recursive calls (X^n/2)*A(X)*B(X)
        second = divide(addition(polyA1, polyA2), addition(polyB1, polyB2))
        second = subtraction(second, shift(divide(polyA2, polyB2), middle))
        second = subtraction(second, divide(polyA1, polyB1))
        for i in range(len(second)):
            result[i+1] += second[i]

        # Last Term A(X)*B(X)
        term = polyA[0] * polyB[0]
        result[0] += term
    print(result)
    return result


# Function to adjust lengths, if needed
def adjust(poly1, poly2):
    if len(poly1) != len(poly2):
        if len(poly1) > len(poly2):
            poly2 = extend(poly2, len(poly1)-len(poly2))
        elif len(poly1) < len(poly2):
            poly1 = extend(poly1, len(poly2)-len(poly1))
    return poly1, poly2


# Function to extend a polynomial
def extend(poly, number):
    for i in range(number):
        poly.append(0)
    return poly


# Function to handle addition: poly1 + poly2
def addition(poly1, poly2):
    poly1, poly2 = adjust(poly1, poly2)
    poly = []
    for i in range(len(poly1)):
        poly.append(poly1[i] + poly2[i])
    return poly


# Function to handle subtraction: poly1 - poly2
def subtraction(poly1, poly2):
    poly1, poly2 = adjust(poly1, poly2)
    poly = []
    for i in range(len(poly1)):
        poly.append(poly1[i] - poly2[i])
    return poly


# Function to shift the terms of a polynomial array a desired degree
def shift(poly, number):
    result = []
    for i in range(number):
        result.append(0)
    for term in poly:
        result.append(term)
    return result


# Function for splitting a polynomial
def split(poly, middle):
    poly1 = []
    poly2 = []
    for i in range(middle):
        poly1.append(poly[i])
    for j in range(middle, middle*2):
        poly2.append(poly[j])
    return poly1, poly2


# Driver for testing
if __name__ == '__main__':
    test1 = [3, -4, 5]  # 5X^2 - 4X + 3
    test2 = [-8, 10]    # 10X -8
    test3 = [0]
    print(divide(test1, test2))  # 50X^3 - 80X^2 + 62X -24 --> [-24, 62, -80, 50, 0]
    print(divide(test1, test3))  # 0 --> [0, 0, 0, 0, 0]

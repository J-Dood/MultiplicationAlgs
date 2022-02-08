# By: Jordan Dood and Christine Johnson
# 2/6/2022
# This code takes two polynomials as vectors and multiplies them using several
# different algorithms and returns a polynomial as a vector.
#
# This file runs the O(n^1.59) divide and conquer algorithm


def divide(polyA, polyB):
    """
    :argument poly1: List
    :argument poly2: List
    :returns: List
    """
    polyA, polyB = adjust(polyA, polyB)
    # Create and populate result list with 0
    result = []
    for i in range(len(polyB)*2 - 1):
        result.append(0)

    # Base Case
    if len(polyA) == 1:
        return polyA[0]*polyB[0]
    # Recursive Case
    else:
        # Make Polynomials even lengths
        if len(polyA)%2 != 0:
            polyA = extend(polyA, 1)
            polyB = extend(polyB, 1)

        # Split the polynomial
        middle = len(polyA)//2
        polyA_1 = polyA[:middle]
        polyA_2 = polyA[middle:]
        polyB_1 = polyB[:middle]
        polyB_2 = polyB[middle:]

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
    for i in range(len(poly1)):
        poly1[i] += poly2[i]
    return poly1


# Function to handle subtraction: poly1 - poly2
def subtraction(poly1, poly2):
    poly1, poly2 = adjust(poly1, poly2)
    for i in range(len(poly1)):
        poly1[i] -= poly2[i]
    return poly1


# Driver for testing
if __name__ == '__main__':
    test1 = [3, -4, 5]  # 5X^2 - 4X + 3
    test2 = [-8, 10]    # 10X -8
    test3 = [0]
    print(divide(test1, test2))  # 50X^3 - 80X^2 + 62X -24 --> [-24, 62, -80, 50, 0]
    print(divide(test1, test3))  # 0 --> [0, 0, 0, 0, 0]

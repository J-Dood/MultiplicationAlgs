# By: Jordan Dood and Christine Johnson
# 2/6/2022
# This code takes two polynomials as vectors and multiplies them using several
# different algorithms and returns a polynomial as a vector.
#
# This file runs the O(n^1.59) conquer and conquer algorithm


def conquer(polyA, polyB):
    """
    :argument polyA: List
    :argument polyB: List
    :returns: List
    """
    polyA, polyB = adjust(polyA, polyB)

    # Base Case
    if len(polyA) == 1:
        return [polyA[0]*polyB[0]]

    # Recursive Case
    else:
        # Make Polynomials even lengths
        if len(polyA)%2 != 0:
            polyA.append(0)
            polyB.append(0)

        # Split the polynomials in half
        middle = len(polyA)//2
        polyA1 = polyA[:middle]
        polyA2 = polyA[middle:]
        polyB1 = polyB[:middle]
        polyB2 = polyB[middle:]

        # Create and populate result list with 0's
        result_len = 2*len(polyA) - 1
        result = []
        for i in range(result_len):
            result.append(0)

        # Lowest Term Regression 1
        firsts = conquer(polyA1, polyB1)
        lowest = firsts

        # Highest Term Regression 2
        seconds = conquer(polyA2, polyB2)
        highest = shift(seconds, len(polyA))

        # Removed Terms Regression 3
        firsts = shift(firsts, len(polyA) // 2)
        seconds = shift(seconds, len(polyB) // 2)
        total = addition(firsts, seconds)

        # Middle terms total
        middle1 = addition(polyA1, polyA2)
        middle2 = addition(polyB1, polyB2)
        multiplication = conquer(middle1, middle2)
        multiplication = shift(multiplication, len(polyA) // 2)

        # Final Results Summation
        result = addition(result, highest)
        result = addition(result, lowest)
        result = addition(result, multiplication)
        result = subtraction(result, total)

    return result


# Function to adjust lengths, if needed
def adjust(poly1, poly2):
    if len(poly1) != len(poly2):
        if len(poly1) > len(poly2):
            poly2 = extend(poly2, len(poly1)-len(poly2))
        elif len(poly1) < len(poly2):
            poly1 = extend(poly1, len(poly2)-len(poly1))
    return poly1, poly2


# Function to extend a polynomial a given number of 0 leading terms
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


# Function to shift the terms of a polynomial array up a Desired number of degrees
def shift(poly, number):
    result = []
    for i in range(number):
        result.append(0)
    for term in poly:
        result.append(term)
    return result


# Driver for testing
if __name__ == '__main__':
    test1 = [3, -4, 5]  # 5X^2 - 4X + 3
    test2 = [-8, 10]    # 10X -8
    test3 = [0]
    test4 = [1, 1]
    test5 = [1, 1, 1, 1]
    test6 = [2, 2, 2, 2]
    print(conquer(test4, test4))  # [1, 2, 1]
    print(conquer(test4, test2))  # [-8, 2, 10]
    print(conquer(test5, test6))  # [2, 4, 6, 8, 6, 4, 2]
    print(conquer(test1, test2))  # 50X^3 - 80X^2 + 62X -24 --> [-24, 62, -80, 50, 0, 0, 0]
    print(conquer(test1, test3))  # [0, 0, 0, 0, 0, 0, 0]

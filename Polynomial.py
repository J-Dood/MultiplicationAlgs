# By: Jordan Dood and Christine Johnson
# 2/6/2022
# This code takes two polynomials as vectors and multiplies them using several
# different algorithms and returns a polynomial as a vector.
#
# This file is the array based polynomial object


# The class stores the coefficients of a polynomial in an array where the index corresponds
# to the degree of the term.


class Polynomial:

    # Constructor
    def __init__(self, coefficients):
        self.coefficients = coefficients

    # Addition Override
    def __add__(self, other):
        new_array = []
        if len(self.coefficients) < len(other.coefficients):
            min = len(self.coefficients)
            dif = len(other.coefficients)-len(self.coefficients)
            flag = True
        elif len(self.coefficients) > len(other.coefficients):
            min = len(other.coefficients)
            dif = len(self.coefficients)-len(other.coefficients)
            flag = False
        for i in range(min):
            new_array.append(self.coefficients[i] + other.coefficients[i])
        for j in range(min, dif + min):
            if flag:
                new_array.append(other.coefficients[j])
            else:
                new_array.append(self.coefficients[j])
        return new_array

    # Subtraction Override
    def __sub__(self, other):
        new_array = []
        if len(self.coefficients) < len(other.coefficients):
            min = len(self.coefficients)
            dif = len(other.coefficients) - len(self.coefficients)
            flag = True
        elif len(self.coefficients) > len(other.coefficients):
            min = len(other.coefficients)
            dif = len(self.coefficients) - len(other.coefficients)
            flag = False
        for i in range(min):
            new_array.append(self.coefficients[i] - other.coefficients[i])
        for j in range(min, dif + min):
            if flag:
                new_array.append(0 - other.coefficients[j])
            else:
                new_array.append(0 - self.coefficients[j])
        return new_array

    # This function returns the maximum term of a polynomial as a string
    def get_max_term(self):
        return str(self.coefficients[len(self.coefficients)]) + "X^" + str(len(self.coefficients))

    # This function returns the minimum term of a polynomial as a string
    def get_min_term(self):
        return str(self.coefficients[0])

    # This function returns all of the terms of a polynomial as a string
    def get_all(self):
        polynomial = "Y(X) ="
        for i in range(len(self.coefficients)):
            if self.coefficients[i] != 0:
                polynomial += (" " + str(self.coefficients[i]) + "X^" + str(i))
        return polynomial


# Driver for testing
if __name__ == '__main__':
    test1 = Polynomial([3, -4, 0, 5])   # 5X^2 - 4X + 3
    test2 = Polynomial([-8, 10])        # 10X -8
    test3 = Polynomial([0])             # 0x
    print(test1 + test2)
    print(test1 - test2)


# By: Jordan Dood and Christine Johnson
# 2/6/2022
# This code takes two polynomials as vectors and multiplies them using several
# different algorithms and returns a polynomial as a vector.
#
# This file generates random polynomials and runs the data collection


# Imports
import random as ran
import Polynomial
import time


# Functions

# A function that returns a random polynomial array of a specified size with coefficients of +-99
def random_array(degree):
    array = []
    for i in range(degree+1):
        array.append(ran.randint(-100, 100))
    return array


# A function that runs a set of 10 size points which are average multiplication time of 20
# randomly generated polynomial multiplications, and prints it.
def data():
    points = [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    for point in points:
        average = 0
        for i in range(20):
            poly1 = Polynomial(random_array(i))
            poly2 = Polynomial(random_array(i))
            start = time()
            # Multiply poly1 and poly2 here
            end = time()
            average += end-start
        print("The Average for degree " + str(point) + " was: " +str(average/20) + " ms")



# Run Option
if __name__ == '__main__':
    data()

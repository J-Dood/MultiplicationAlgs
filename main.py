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
from ConquerAlg import conquer
from NaiveAlg import naive


def random_array(degree):
    array = []
    for i in range(degree+1):
        array.append(ran.randint(-100, 100))
    return array


# A function that runs a set of 10 size points which are average multiplication time of 20
# randomly generated polynomial multiplications, and prints it.
def data1():
    points = [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    for point in points:
        average = 0
        for i in range(20):
            poly1 = random_array(point)
            poly2 = random_array(point)
            start = time.time()
            product = conquer(poly1, poly2)
            end = time.time()
            if (end-start)*1000 > 600000:
                print(str((end-start)*1000) + " :Ten min limit passed!!")
                return
            average += end-start
        print("The Average for degree " + str(point) + " was: " +str(average*1000/20) + " ms")

def data2():
    points = [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    for point in points:
        average = 0
        for i in range(20):
            poly1 = random_array(point)
            poly2 = random_array(point)
            start = time.time()
            product = naive(poly1, poly2)
            end = time.time()
            if (end-start)*1000 > 600000:
                print(str((end-start)*1000) + " :Ten min limit passed!!")
                return
            average += end-start
        print("The Average for degree " + str(point) + " was: " +str(average*1000/20) + " ms")

# Run Option
if __name__ == '__main__':
    data1()
    data2()

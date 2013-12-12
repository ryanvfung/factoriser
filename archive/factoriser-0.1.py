# -*- coding: utf-8 -*-
""" Integer Factoriser 0.1
    @author: Ryan Fung
    Create Date: 2013-10-15
"""
# input("Enter a number to be factorised:")


def f(n):
    return factorise(n)


def factorise(number):
    """Given an integer, returns a list of of prime factors"""
    n = number
    s = n**0.5
    factors = 0
    factorList = []

    if type(n) != int:
        return "Error: argument must be an integer"
    if (n <= 1):
        return "Error: argument must be greater than one (1)"
    # Begin checking for factors
    for factor in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        while checkFactor(n, factor):
            n = n / factor
            s = n**0.5
            factors += 1
            factorList.append(factor)
            foundFactor(factor, factors, factorList)
        if (n == 1) or (s > n):
            break
    a = 0
    while n != 1 and s > factor:
        for factor in [31+a, 37+a, 41+a, 43+a, 47+a, 49+a, 53+a, 59+a]:
            while checkFactor(n, factor):
                n = n / factor
                s = n**0.5
                factors += 1
                factorList.append(factor)
                foundFactor(factor, factors, factorList)
        a += 30
    print("----------\nFactorisation complete:")
    if factorList == []:
        factorList = [number]
    if factorList[0] == number:
        print(str(number) + " is prime")
    else:
        print("Found the following factors: " + str(factorList))
    return factorList


def checkFactor(number, factor):
    """Check if number is divisible by factor:
    if divisible, prints result and returns with the dividend;
    if not divisible, returns with original number"""
    if number == 1:
        return False
    if number % factor == 0:
        return True
    else:
        return False


def foundFactor(factor, factors, factorList):
    """Print factor result with current factor list"""
    print("-----")
    print("Found factor " + str(factors) + ": " + str(factor))
    print("Current Factor List:" + str(factorList))

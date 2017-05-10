# Special Pythagorean triplet
# https://projecteuler.net/problem=9

import math

# Checks if n is a square
def isSquare(n):
	return True if math.sqrt(n) % 1 == 0 else False

# Finds Pythagorean triplet with sum of n, with largest c value possible
def findTripletBySum(n):
	if n < 6: return None
	for c in range(n - 2, 3, -1):
		for b in range(n - c - 1, 2, -1):
			a = n - b - c
			if a ** 2 + b ** 2 == c ** 2:
				return a, b, c
	return None

# Returns product of all elements in list or tuple l
def productOfList(l):
	if not l:
		return None
	product = 1
	for number in l:
		product *= number
	return product

print(productOfList(findTripletBySum(1000)))
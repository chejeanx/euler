# Spiral primes
# https://projecteuler.net/problem=58

import math

# Checks if n is prime
def isPrime(n):
	if n < 2: return False
	if n == 2: return True
	for factor in range(2, math.ceil(math.sqrt(n)) + 1):
		if n % factor == 0:
			return False
	return True

# Returns side length of the square spiral for which the ratio of primes along both diagonals first falls below percentage
def spiralPrimeDiagonals(percentage):
	sideLength = 3
	value = 9
	numPrimes = 3

	while numPrimes / (2 * sideLength - 1) >= percentage:
		for corner in range(0, 3):
			value += (sideLength + 1)
			if isPrime(value):
				numPrimes += 1
		# Don't have to check 4th corner, we know it's an odd square on the bottom right diagonal
		value += (sideLength + 1)
		sideLength += 2
	return sideLength

print(spiralPrimeDiagonals(0.1))
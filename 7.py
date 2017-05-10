# 10001st prime
# https://projecteuler.net/problem=7

import math

# Checks if n is prime
def isPrime(n):
	if n < 2: return False
	if n == 2: return True
	else:
		for factor in range(2, math.ceil(math.sqrt(n)) + 1):
			if n % factor == 0:
				return False
	return True

# Returns nth prime
def nthPrime(n):
	prime = 2
	testValue = 3
	while n > 1:
		if isPrime(testValue):
			n -= 1
			prime = testValue
		testValue += 2
	return prime

print(nthPrime(10001))
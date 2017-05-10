# Circular primes
# https://projecteuler.net/problem=35

import math

# Sieve of Erastosthenes returning primes up to including n
def sieveOfErastosthenes(n):
	isPrime = [True] * (n + 1)
	isPrime[0] = isPrime[1] = False
	primes = []
	for value in range(n + 1):
		if isPrime[value]:
			primes.append(value)
			for multiple in range(value * 2, n + 1, value):
				isPrime[multiple] = False
	return primes

# Returns whether n is prime
def isPrime(n):
	if n < 2: return False
	if n == 2: return True
	else:
		for factor in range(2, math.ceil(math.sqrt(n)) + 1):
			if n % factor == 0:
				return False
	return True

# Returns list of circle numbers for n
def circleNumbers(n):
	circleList = []
	numDigits = 0
	num = n
	while num > 0:
		numDigits += 1
		num //= 10
	numCircles = numDigits
	while numCircles > 0:
		n = (n - (n % 10)) // 10 + ((n % 10) * 10 ** (numDigits - 1))
		circleList.append(n)
		numCircles -= 1
	return circleList

# Returns number of circular primes below n
def numCircularPrimes(n):
	count = 0
	for prime in sieveOfErastosthenes(n):
		isCirclePrime = True
		for circleNum in circleNumbers(prime):
			if not isPrime(circleNum):
				isCirclePrime = False
				break
		if isCirclePrime:
			count += 1
	return count

print(numCircularPrimes(1000000))

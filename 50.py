# Consecutive prime sum
# https://projecteuler.net/problem=50

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

# Finds smallest sieve threshold needed for sum of all primes to be less than n
def smallestSieveThresholdForSum(n):
	number = 1
	while sum(sieveOfErastosthenes(number)) < n:
		number += 1
	return number - 1

# Finds prime below n that can be written as sum of most consecutive primes
def primeSumOfMostConsecutivePrimes(n):
	primes = sieveOfErastosthenes(smallestSieveThresholdForSum(n))
	currentTerms = len(primes)
	currentPrime = 0
	startIndex = 0
	while currentTerms > 0:
		while len(primes) - startIndex >= currentTerms:
			currentSum = sum(primes[startIndex:startIndex + currentTerms])
			if currentSum < n:
				if isPrime(currentSum):
					return currentSum
			startIndex += 1
		startIndex = 0
		currentTerms -= 1
	return 0

print(primeSumOfMostConsecutivePrimes(1000000))










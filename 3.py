# Largest prime factor
# https://projecteuler.net/problem=3

import math

# Checks if f is a factor of n
def isFactor(f, n):
	if (n == 0): return True
	elif (f == 0): return False
	else: return (n % f ==0)

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

# Returns largest prime factor of n
def largestPrimeFactor(n):
	sieve = sieveOfErastosthenes(math.floor(math.sqrt(n)))
	for index in range(len(sieve) - 1, 0, -1):
		if isFactor(sieve[index], n):
			return sieve[index]
	return None

print(largestPrimeFactor(600851475143))
# Smallest multiple
# https://projecteuler.net/problem=5

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

# Returns prime factorization list of n or list of n if n is prime
def primeFactorization(n):
	factors = []
	if sieveOfErastosthenes(n)[-1] == n:
		return [n]

	primeList = sieveOfErastosthenes(n // 2 + 1)
	while n > 1:
		for prime in primeList:
			if n % prime == 0:
				factors.append(prime)
				n /= prime

	return factors

# Returns smallest positive number that is evenly divisible by all numbers from 1 to n
def smallestPossibleDivisor(n):
	factorMap = {}
	for factor in sieveOfErastosthenes(n):
		factorMap[factor] = 1

	for number in range(2, n + 1):
		tempFactorMap = factorMap.copy()
		primeFactorList = primeFactorization(number)
		for primeFactor in primeFactorList:
			if primeFactor in tempFactorMap:
				if tempFactorMap[primeFactor] == 1:
					del tempFactorMap[primeFactor]
				else:
					tempFactorMap[primeFactor] -= 1
			else:
				if primeFactor in factorMap:
					factorMap[primeFactor] += 1
				else:
					factorMap[primeFactor] = 1

	smallestDivisor = 1
	for factor in factorMap:
		smallestDivisor *= factor ** factorMap[factor]

	return smallestDivisor

print(smallestPossibleDivisor(20))
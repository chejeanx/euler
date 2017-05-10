# Summation of primes
# https://projecteuler.net/problem=10

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

# Sum of all primes below n
def sumOfPrimes(n):
	sieve = sieveOfErastosthenes(n - 1)
	return sum(sieve)

print(sumOfPrimes(2000000))
# Pandigital prime
# https://projecteuler.net/problem=41

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

# Returns true if number contains digits 1 to number of digits exactly once, false otherwise
def isPandigital(n):
	if len(str(n)) > 9:
		return False

	for index in range(len(str(n))):
		if index != int(sorted(str(n))[index]) - 1:
			return False
	return True

# Returns largest prime with only unique digits
def largestPandigitalPrime():
	sieve = sieveOfErastosthenes(987654321)
	for prime in sieve[::-1]:
		if isPandigital(prime):
			return prime

print(largestPandigitalPrime())

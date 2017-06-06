# Distinct primes factors
# https://projecteuler.net/problem=47

# Sieve of Erastosthenes returning primes up to including n
def sieveOfErastosthenes(n):
	isPrime = [True] * (n + 1)
	isPrime[0] = isPrime[1] = False
	primes = []
	for value in range(0, n + 1):
		if isPrime[value]:
			primes.append(value)
			for multiple in range(value * 2, n + 1, value):
				isPrime[multiple] = False
	return primes

# Return first number of first c consecutive numbers with d distinct prime factors below maxNum using sieveSize for largest prime to test 
def distinctPrimeFactors(c, d, sieveSize, maxNum):
	# May need more primes depending on how big c and d are, this is for c = 4, d = 4
	sieve = sieveOfErastosthenes(sieveSize)
	currentPrime = 2
	currentChain = []
	for testNum in range(2, maxNum + 1):
		currentNum = testNum
		currentIndex = 0
		currentFactors = 0
		while currentIndex < len(sieve) and currentNum != 1 and currentFactors < d:
			if currentNum % sieve[currentIndex] == 0:
				currentFactors += 1
			while currentNum % sieve[currentIndex] == 0:
				currentNum //= sieve[currentIndex]
			currentIndex += 1
		if currentNum == 1 and currentFactors == d:
			currentChain.append(testNum)
		else:
			currentChain = []
		if len(currentChain) == c:
			return currentChain[0]
	return None

print(distinctPrimeFactors(4, 4, 1000, 1000000))
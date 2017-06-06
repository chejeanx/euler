# Prime permutations
# https://projecteuler.net/problem=49

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

# Returns list of prime permutations in increasing order of primes containing numDigits digits, and where there are at least numElements permutations of those digits
def primePermutations(numDigits, numElements):
	if numDigits < 4 or numElements < 2:
		return None

	# Get sieve of all primes with numDigits
	sieve = sieveOfErastosthenes(10 ** numDigits - 1)
	lowestPrimeIndex = 0
	while sieve[lowestPrimeIndex] < 10 ** (numDigits - 1) + 1:
		lowestPrimeIndex += 1
	sieve = sieve[lowestPrimeIndex:]

	# Make dictionary where key is the sorted prime in increasing digit order, and value is a list of primes that are permutations of that key
	primeListDict = {}
	for prime in sieve:
		sortedPrimeDigits = int(''.join(sorted(str(prime))))
		if sortedPrimeDigits not in primeListDict:
			primeListDict[sortedPrimeDigits] = [prime]
		else:
			primeListDict[sortedPrimeDigits].append(prime)

	# Create list of prime permutations with numElements elements or more
	primePerms = []
	for primeList in primeListDict:
		if len(primeListDict[primeList]) >= numElements:
			primePerms.append(primeListDict[primeList])

	return primePerms

# Returns list of arithmetic sequences contained within each sequence in a list of sequences
def arithmeticSequences(sequences):
	arithmeticSeqs = []
	for sequence in sequences:
		sequence = sorted(sequence)
		for index1 in range(len(sequence)):
			for index2 in range(index1 + 1, len(sequence)):
				currentDiff = sequence[index2] - sequence[index1]
				for element in sequence[index2 + 1:]:
					if sequence[index2] + currentDiff == element:
						arithmeticSeqs.append([sequence[index1], sequence[index2], element])
	return arithmeticSeqs

print (arithmeticSequences(primePermutations(4, 3)))
print ([str(a) + str(b) + str(c) for a, b, c in arithmeticSequences(primePermutations(4, 3))])

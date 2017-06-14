# Combinatoric selections
# https://projecteuler.net/problem=53

# Returns n!
def factorial(n):
	return 1 if n <= 1 else n * factorial(n - 1)

# Returns combinations of nCr, r <= n
def combinations(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

# Returns number of combinations nCr that are greater than threshold
def bigCombos(minN, maxN, threshold):
	count = 0
	for n in range(minN, maxN + 1):
		for r in range(0, n + 1):
			if combinations(n, r) > threshold:
				count += 1
	return count

print(bigCombos(1, 100, 1000000))

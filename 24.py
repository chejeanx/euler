# Lexicographic permutations
# https://projecteuler.net/problem=24

# Returns n!
def factorial(n):
	if n <= 1: return 1
	else: return n * factorial(n - 1)

# Returns nth lexicographic permutation of numbers from 0 to maxDigit
def nthLexicographicPermutation(n, maxDigit):
	if n > factorial(maxDigit + 1) or maxDigit > 9:
		return None

	remainingDigits = [digit for digit in range(0, maxDigit + 1)]
	lexico = ''

	while len(remainingDigits) > 0:	
		index = 0
		section = factorial(len(remainingDigits) - 1)
		while index < len(remainingDigits) - 1 and section < n:
			section += factorial(len(remainingDigits) - 1)
			index += 1
		section -= factorial(len(remainingDigits) - 1)
		n -= section
		lexico += str(remainingDigits.pop(index))

	return lexico

print(nthLexicographicPermutation(1000000, 9))
# Number letter counts
# https://projecteuler.net/problem=17

# Returns kth digit in n, starting at index 0 rightmost
def kthDigit(n, k):
	return (abs(n) // 10 ** k % 10)

# Creates hash map of number of letters for numbers up to 1000
def numLettersForNumbers():
	numLetters = {
		1: 3,
		2: 3,
		3: 5,
		4: 4,
		5: 4,
		6: 3,
		7: 5,
		8: 5,
		9: 4,
		10: 3,
		11: 6,
		12: 6,
		13: 8,
		14: 8,
		15: 7,
		16: 7,
		17: 9,
		18: 8,
		19: 8,
		20: 6,
		30: 6,
		40: 5,
		50: 5,
		60: 5,
		70: 7,
		80: 6,
		90: 6,
		100: 7,
		1000: 8
	}
	return numLetters

# Returns number of letters for a single postive number n up to 9999
def numLetters(n):
	numLetters = numLettersForNumbers()
	total = 0

	if n >= 10000:
		return None

	while n > 0:
		if n >= 1000:
			total += (numLetters[1000] + numLetters[kthDigit(n, 3)])
			n -= (kthDigit(n, 3) * 1000)
		elif n >= 100:
			# Account for 'and' in numbers above 100 with trailing digits
			if n % 100 != 0:
				total += 3
			total += (numLetters[100] + numLetters[kthDigit(n, 2)])
			n -= (kthDigit(n, 2) * 100)
		elif n >= 20:
			total += numLetters[kthDigit(n, 1) * 10]
			n -= (kthDigit(n, 1) * 10)
		else:
			total += numLetters[n]
			n -= n

	return total

# Returns number of letters for all numbers in range n to m inclusive up to max 9999
def totalNumLetters(n, m):
	if not n < m or m >= 10000:
		return None

	total = 0
	for number in range(n, m + 1):
		total += numLetters(number)
	return total

print(totalNumLetters(1, 1000))



	
	
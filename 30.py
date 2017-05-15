# Digit fifth powers
# https://projecteuler.net/problem=30

# Find sum of kth powers of all digits of a number
def sumOfKthPowersOfDigits(n, k):
	total = 0
	while n > 0:
		total += (n % 10) ** k
		n //= 10
	return total

# Find max number (by power of 10s - also number of digits) to check for kth power
def maxNumToCheckForSumOfPowers(k):
	numDigits = 1
	while 9 ** k * numDigits > 10 ** numDigits:
		numDigits += 1
	return 10 ** numDigits

# Find sum of all numbers that can be written as kth powers of all their digits not including 1
def sumOfDigitKthPowers(k):
	total = 0
	for x in range(2, maxNumToCheckForSumOfPowers(k) + 1):
		if sumOfKthPowersOfDigits(x, k) == x:
			total += x
	return total

print(sumOfDigitKthPowers(5))
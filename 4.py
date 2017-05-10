# Largest palindrome product
# https://projecteuler.net/problem=4

# Checks if number is a palindrome (without string functions)
def isPalindromeNumber(n):
	num = n
	rev = 0
	while n > 0:
		rev = rev * 10 + n % 10
		n //= 10
	return num == rev

# Counts number of digits in a number
def numDigits(n):
	total = 0
	while n > 0:
		total += 1
		n //= 10
	return total

# Checks if number n is a product of two k digit numbers
def checkIfProduct(n, k):
	maxPossibleFactor = 10 ** (k) - 1
	minPossibleFactor = 10 ** (k - 1)

	for number in range(maxPossibleFactor, minPossibleFactor, -1):
		if n % number == 0:
			otherFactor = n / number
			if numDigits(otherFactor) == k:
				return True

	return False

# Finds largest palindrome from product of two k digit numbers
def largestPalindromeProduct(k):
	maxPossibleFactor = 10 ** (k) - 1
	minPossibleFactor = 10 ** (k - 1)

	for number in range(maxPossibleFactor ** 2, minPossibleFactor ** 2, -1):
		if isPalindromeNumber(number):
			if checkIfProduct(number, k):
				return number

	return None

print(largestPalindromeProduct(3))





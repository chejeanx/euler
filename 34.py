# Digit factorials
# https://projecteuler.net/problem=34

# Returns n!
def factorial(n):
	if n <= 1: return 1
	else: return n * factorial(n - 1)

# Find max number (by power of 10s - also number of digits) to check for factorials of digits equalling the number
def maxNumToCheckForSumOfFactorials():
	numDigits = 1
	while factorial(9) * numDigits > 10 ** numDigits:
		numDigits += 1
	return factorial(9) * numDigits

# Returns map of factorials for 0 to n not including n
def factorialMap(n):
	factorials = {}
	for number in range(0, n):
		factorials[number] = factorial(number)
	return factorials

# Returns sum of factorials of all digits of n
def sumOfFactorialsOfDigits(n):
	factorials = factorialMap(10)
	total = 0
	number = n
	while number > 0:
		total += factorials[number % 10]
		number //= 10	
	return total

# Returns sum of all numbers which are equal to the sum of the factorial of their digits (not including 1 and 2)
def sumOfDigitFactorials():
	total = 0
	for x in range(3, maxNumToCheckForSumOfFactorials() + 1):
		if sumOfFactorialsOfDigits(x) == x:
			print(x)
			total += x
	return total

print (sumOfDigitFactorials())
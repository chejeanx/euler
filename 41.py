# Pandigital prime
# https://projecteuler.net/problem=41

import math

# Checks if n is prime
def isPrime(n):
	if n < 2: return False
	if n == 2: return True
	for factor in range(2, math.ceil(math.sqrt(n)) + 1):
		if n % factor == 0:
			return False
	return True

# Returns n!
def factorial(n):
	return 1 if n <= 1 else n * factorial(n - 1)

# Returns permutations of items in inpList in a list
def getPermutations(inpList):
	numPerms = factorial(len(inpList))
	answer = []
	
	def getPerms(current, inpList):
		if len(inpList) == 0:
			answer.append(current)
		if len(answer) == numPerms:
			return
		for i in range(len(inpList)):
			getPerms(current + str(inpList[i]), inpList[:i] + inpList[i + 1:])
	
	getPerms('', inpList)
	return answer

# Returns largest prime up to maxDigits in length with only unique digits
def largestPandigitalPrime(maxDigits):
	if maxDigits <= 0 or maxDigits > 9:
		return None

	digits = []
	pandigitalNums = []
	for digit in range(1, maxDigits + 1):
		digits.append(digit)
		pandigitalNums += getPermutations(digits)
	for pandigital in pandigitalNums[::-1]:
		if isPrime(int(pandigital)):
			return int(pandigital)
	return None

print(largestPandigitalPrime(9))

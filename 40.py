# Champernowne's constant
# https://projecteuler.net/problem=40

import math

# Returns kth digit in n, starting at index 0 rightmost
def kthDigit(n, k):
	return (abs(n) // 10 ** k % 10)

# Returns nth digit of Champernowne's constant
def nthChampernowneDigit(n):
	numDigits = 1
	while n > 9 * 10 ** (numDigits - 1) * numDigits:
		n -= 9 * 10 ** (numDigits - 1) * numDigits
		numDigits += 1

	# Use the cardinal number found at nth digit and the digit placement of that number to find the final digit
	numAt = 10 ** (numDigits - 1) + math.ceil(n / numDigits) - 1
	digitOfNum = numDigits if n % numDigits == 0 else n % numDigits
	return kthDigit(numAt, numDigits - digitOfNum)

print(nthChampernowneDigit(1) * nthChampernowneDigit(10) * nthChampernowneDigit(100) * nthChampernowneDigit(1000) * nthChampernowneDigit(10000) * nthChampernowneDigit(100000) * nthChampernowneDigit(1000000))
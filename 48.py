# Self powers
# https://projecteuler.net/problem=48

# Finds last digits (not including preceding 0s) of series 1^1 + 2^2 + 3^3 ... numTermsInSeries^numTermsInSeries
def findLastDigits(numTermsInSeries, numLastDigits):
	lastDigits = 0
	for num in range(1, numTermsInSeries + 1):
		truncatedNum = (num ** num) % (10 ** 10)
		lastDigits += truncatedNum
		lastDigits = lastDigits % (10 ** 10)
	return lastDigits

print(findLastDigits(1000, 10))
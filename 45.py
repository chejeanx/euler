# Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45

import math

# Math for triangular:
# x = n(n + 1) / 2
# 8x = 8n(n + 1) / 2 = 4n(n + 1) = 4n^2 + 4n
# 8x + 1 = 4n^2 + 4n + 1 = (2n + 1)^2
# Therefore if 8x + 1 is an odd perfect square, x is triangular
def isTriangular(x):
	return math.sqrt(8 * x + 1) % 1 == 0 and math.sqrt(8 * x + 1) % 2 == 1

# Math for pentagonal:
# x = n(3n - 1) / 2
# 24x = 24n(3n - 1) / 2 = 12n(3n - 1) = 36n^2 - 12n
# 24x + 1 = 36n^2 - 12n + 1
# sqrt(24x + 1) = (6n - 1)^2 or (1 - 6n)^2
# Therefore if (sqrt(24x + 1) + 1) / 6 is an integer, x is pentagonal (can also check if (sqrt(24x + 1) - 1) / -6 is an integer)
def isPentagonal(x):
	return ((math.sqrt(24 * x + 1) + 1) / 6) % 1 == 0

# Math for hexagonal (just for fun):
# x = n(2n - 1)
# 8x = 8n(2n - 1) = 16n^2 - 8n
# 8x + 1 = 16n^2 - 8n + 1 = (4n - 1)^2 or (1 - 4n)^2
# Therefore if (sqrt(8x + 1) + 1) / 4 is an integer, x is hexagonal (can also check if (sqrt(8x + 1) - 1) / -4 is an integer)
def isHexagonal(x):
	return ((math.sqrt(8 * x + 1) + 1) / 4) % 1 == 0

# Returns first n numbers that are all three triangular, pentagonal and hexagonal
def firstTriPentHexNums(n):
	index = 1
	answerList = []
	while len(answerList) < n:
		currentHex = index * (2 * index - 1)
		if isTriangular(currentHex) and isPentagonal(currentHex):
			answerList.append(currentHex)
		index += 1
	return answerList

print(firstTriPentHexNums(3))
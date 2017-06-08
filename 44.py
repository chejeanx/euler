# Pentagon numbers
# https://projecteuler.net/problem=44

import math

# Math for pentagonal:
# x = n(3n - 1) / 2
# 24x = 24n(3n - 1) / 2 = 12n(3n - 1) = 36n^2 - 12n
# 24x + 1 = 36n^2 - 12n + 1
# sqrt(24x + 1) = (6n - 1)^2 or (1 - 6n)^2
# Therefore if (sqrt(24x + 1) + 1) / 6 is an integer, x is pentagonal (can also check if (sqrt(24x + 1) - 1) / -6 is an integer)
def isPentagonal(x):
	return ((math.sqrt(24 * x + 1) + 1) / 6) % 1 == 0

# Returns pair of pentagonal numbers whose sum and difference are also pentagonal and their difference is minimised
def closestPentagonPairDiff():
	pentagonList = []
	difference = 0
	while difference == 0 or pentagonList[-1] - pentagonList[0] < difference:
		pentagonList.append(int((len(pentagonList) + 1) * ((3 * (len(pentagonList) + 1) - 1) / 2)))
		for pentagon in pentagonList[-2::-1]:
			if isPentagonal(pentagonList[-1] - pentagon) and isPentagonal(pentagonList[-1] + pentagon):
				if difference == 0 or pentagonList[-1] - pentagon < difference:
					difference = pentagonList[-1] - pentagon
	return difference

print(closestPentagonPairDiff())
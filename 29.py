# Distinct powers
# https://projecteuler.net/problem=29

# Returns number of distinct terms generated by a ** b
def distinctPowers(minA, maxA, minB, maxB):
	powerDict = {}
	for a in range(minA, maxA + 1):
		for b in range(minB, maxB + 1):
			powerDict[a ** b] = 1
	return len(powerDict)

print(distinctPowers(2, 100, 2, 100))
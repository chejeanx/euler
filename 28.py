# Number spiral diagonals
# https://projecteuler.net/problem=28

# Returns sum of numbers on diagonals on n x n spiral
def sumOfSpiralDiagonals(n):
	if n % 2 == 0: return None
	total = 1
	value = 1
	for increment in range(2, n, 2):
		for corner in range(0, 4):
			value += increment
			total += value
	return total

print(sumOfSpiralDiagonals(1001))
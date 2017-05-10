# Sum square difference
# https://projecteuler.net/problem=6

# Returns sum of squares of first n numbers
def sumOfSquares(n):
	total = 0
	for number in range(n + 1):
		total += number ** 2
	return total

# Returns square of sum of first n numbers
def squareOfSum(n):
	total = 0
	for number in range(n + 1):
		total += number
	return total ** 2

# Returns difference between sum of squares and the square of the sum for first n numbers
def diffSumOfSquaresAndSquareOfSum(n):
	return abs(sumOfSquares(n) - squareOfSum(n))

print(diffSumOfSquaresAndSquareOfSum(100))

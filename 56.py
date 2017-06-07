# Powerful digit sum
# https://projecteuler.net/problem=56

# Returns sum of n's digits
def sumOfDigits(n):
	return sum(int(x) for x in str(n) if x.isdigit())

# Returns max digital sum of a ** b for all values of a from 1 to maxNum and all values of b from 1 to maxNum
def powerfulDigitSum(maxNum):
	return max([sumOfDigits(element) for element in {a ** b for b in range(1, maxNum + 1) for a in range(0, maxNum + 1)}])

print(powerfulDigitSum(100))
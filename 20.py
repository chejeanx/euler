# Factorial digit sum
# https://projecteuler.net/problem=20

# Returns n!
def factorial(n):
	if n <= 1: return 1
	else: return n * factorial(n - 1)

# Returns sum of digits in n
def sumOfDigits(n):
	total = 0
	while n > 0:
		total += n % 10
		n //= 10
	return total

print(sumOfDigits(factorial(100)))
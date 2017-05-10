# Power digit sum
# https://projecteuler.net/problem=16

# Returns sum of n's digits
def sumOfDigits(n):
	total = 0
	while n > 0:
		total += n % 10
		n //= 10
	return total

print(sumOfDigits(2 ** 1000))
# Multiples of 3 and 5
# https://projecteuler.net/problem=1

# Returns sum of multiples of 3 or 5 below n
def sumOfMultiples(n):
	total = 0
	for x in range(3, n):
		if x % 3 == 0 or x % 5 == 0:
			total += x
	return total

print(sumOfMultiples(1000)) 
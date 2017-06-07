# Highly divisible triangular number
# https://projecteuler.net/problem=12

# Returns all divisors of n, including n, in a list
def getDivisorsIncludingN(n):
	divisors = [1]
	for number in range(2, n // 2 + 1):
		if n % number == 0:
			divisors.append(number)
	if n != 1:
		divisors.append(n)
	return divisors

# Returns the nth triangle number
def nthTriangleNumber(n):
	triangleNumber = 0
	while n > 0:
		triangleNumber += n
		n -= 1
	return triangleNumber

# Returns 1st triangle number to have over k divisors
def firstTriangleNumberByDivisors(k):
	numDivisors = 1
	index = 1
	triangleNumber = 1

	while numDivisors <= k:
		index += 1
		triangleNumber += index
		# print(triangleNumber)
		numDivisors = len(getDivisorsIncludingN(triangleNumber))

	return triangleNumber

print(firstTriangleNumberByDivisors(500))
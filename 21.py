# Amicable numbers
# https://projecteuler.net/problem=21

# Returns all divisors of n, not including n, in a list
def getDivisors(n):
	divisors = [1]
	for number in range(2, n // 2 + 1):
		if n % number == 0:
			divisors.append(number)
	return divisors

# Returns amicable numbers under n in a list
def amicableNumbers(n):
	amicableMap = {}
	for number in range(2, n):
		amicableMap[number] = None
	amicables = []
	for number1 in range(2, n):
		if amicableMap[number1] == None:
			number2 = sum(getDivisors(number1))
			if number2 < n:
				divisorSumOfNumber2 = sum(getDivisors(number2))
				if number1 == divisorSumOfNumber2 and number1 != number2:
					amicableMap[number1] = True
					amicableMap[number2] = True
					amicables.extend((number1, number2))
				else:
					amicableMap[number1] = False
					amicableMap[number2] = False
	return amicables

print(sum(amicableNumbers(10000)))


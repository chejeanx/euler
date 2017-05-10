# Even Fibonacci numbers
# https://projecteuler.net/problem=2

# Returns Fibonacci terms less than n in a list
def fibonacciList(n):
	fibonacci = [1, 2]
	index = 2
	current = 3
	while current < n:
		fibonacci.append(current)
		index += 1
		current = fibonacci[index-1] + fibonacci[index-2]
	return fibonacci

# Returns sum of even numbers in list
def sumOfEvens(sequence):
	total = 0
	for number in sequence:
		if number % 2 == 0:
			total += number
	return total

print(sumOfEvens(fibonacciList(4000000)))
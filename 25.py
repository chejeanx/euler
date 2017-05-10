# 1000-digit Fibonacci number
# https://projecteuler.net/problem=25

# Returns index of first term in Fibonacci sequence containing n digits (n > 1)
def fibonacciNumDigits(n):
	index = 3
	previous = 1
	term = 2
	while (term < 10 ** (n - 1)):
		previous, term = term, term + previous
		index += 1
	return index

print(fibonacciNumDigits(1000))
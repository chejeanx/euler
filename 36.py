# Double-base palindromes
# https://projecteuler.net/problem=36

# Checks if number is a palindrome (without string functions)
def isPalindromeNumber(n):
	num = n
	rev = 0
	while n > 0:
		rev = rev * 10 + n % 10
		n //= 10
	return num == rev

# Converts number from base 10 to base k
def baseConversion(n, k):
	answer = ''
	currentPlace = 0
	while n > 0:
		answer = str(n % k) + answer
		currentPlace += 1
		n //= k
	answer = int(answer)
	return answer

# Converts number from base 10 to base 2 (uses python bin function)
def base2Conversion(n):
	return int(str(bin(n))[2:])

# Returns sum of palindromes in base 10 and base 2 under n
def sumOfPalindromesInBase10AndBase2(n):
	total = 0
	for number in range(1, n):
		if isPalindromeNumber(number) and isPalindromeNumber(base2Conversion(number)):
			total += number
	return total

print(sumOfPalindromesInBase10AndBase2(1000000))

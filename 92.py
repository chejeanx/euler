# Square digit chains
# https://projecteuler.net/problem=92

# Returns terminating number in square digit chain for startN
def squareDigitChain(startN, currentN, chainOutcomes):
	if currentN == 1 or currentN == 89: 
		chainOutcomes[startN] = currentN
		return currentN
	if currentN in chainOutcomes:
		return chainOutcomes[currentN]
	answer = 0
	for char in str(currentN):
		answer += int(char) ** 2
	return squareDigitChain(startN, answer, chainOutcomes)

# Returns number of numbers below maxNum that terminate their square digit chains at 89
def squareDigit89s(maxNum):
	num89s = 0
	for num in range(1, maxNum):
		if num % 10000 == 0: print(num)
		if squareDigitChain(num, num, {}) == 89:
			num89s += 1
	return num89s

print(squareDigit89s(10000000))
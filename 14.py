# Longest Collatz sequence
# https://projecteuler.net/problem=14

# Returns Collatz sequence starting at n as a list
def collatzSequence(n):
	collatzSeq = []
	currentTerm = abs(n)
	while currentTerm > 1:
		collatzSeq.append(currentTerm)
		if currentTerm % 2 == 0:
			currentTerm //= 2
		else:
			currentTerm = currentTerm * 3 + 1
	collatzSeq.append(1)
	return collatzSeq

# Returns length of Collatz sequence starting at n
def collatzSequenceLength(n):
	return len(collatzSequence(n))

# Returns longest chain of Collatz sequence with starting number less than n
def longestCollatzSequenceChain(n):
	startingNumber = 0
	longestChain = 0
	for testStart in range(n - 1, 2, -1):
		if collatzSequenceLength(testStart) > longestChain:
			longestChain = collatzSequenceLength(testStart)
			startingNumber = testStart
	return startingNumber

print(longestCollatzSequenceChain(1000000))






# Permuted multiples
# https://projecteuler.net/problem=52

# Returns smallest postive integer x such that 1x, 2x, ... multiplier*x contain the same digits
def smallestPermutedMultiple(multiplier):
	current = 1
	answer = 0

	while answer == 0:
		for mult in range(2, multiplier + 1):
			if len(str(mult * current)) == len(str(current)) and sorted(str(mult * current)) == sorted(str(current)):
				if mult == multiplier:
					answer = current
			else:
				break
		current += 1

	return answer

print(smallestPermutedMultiple(6))

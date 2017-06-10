# Coded triangle numbers
# https://projecteuler.net/problem=42

import math

# Math for triangular:
# x = n(n + 1) / 2
# 8x = 8n(n + 1) / 2 = 4n(n + 1) = 4n^2 + 4n
# 8x + 1 = 4n^2 + 4n + 1 = (2n + 1)^2
# Therefore if 8x + 1 is an odd perfect square, x is triangular
def isTriangular(x):
	return math.sqrt(8 * x + 1) % 1 == 0 and math.sqrt(8 * x + 1) % 2 == 1

# Simple reading file function
def readFile(path):
	with open(path, 'r+') as f:
		return f.read()

# Returns list of values in text, separated by comma and removing quotation marks
def listOfWordValues(text):
	return [word[1:-1] for word in text.split(',')]

# Returns number of triangle words based on sum of letter scores in file
def numTriangleWords(filename):
	alphaScores = {}
	for alphaIndex in range(26):
		alphaScores[chr(65 + alphaIndex)] = alphaIndex + 1

	triangleWords = 0
	for word in listOfWordValues(readFile(filename)):
		wordScore = sum([alphaScores[char] for char in word])
		if isTriangular(wordScore):
			triangleWords += 1
	return triangleWords

print(numTriangleWords('p042_words.txt'))

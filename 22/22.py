# Names scores
# https://projecteuler.net/problem=22

# Simple reading file function
def readFile(path):
	with open(path, 'r+') as f:
		return f.read()

# Returns list of values in text, separated by comma and removing quotation marks
def listOfNameValues(text):
	namesRead = text.split(',')
	nameValues = []
	for name in namesRead:
		nameValues.append(name[1:-1])
	return nameValues

# Returns score of a single name, based on alphabetical position of letters
def scoreName(name):
	alphaScores = {}
	alphaIndex = 0
	while alphaIndex < 26:
		alphaScores[chr(65 + alphaIndex)] = alphaIndex + 1
		alphaIndex += 1
	
	nameScore = 0
	for character in name:
		nameScore += alphaScores[character]

	return nameScore

# Returns score of all names in file, each multiplied by its alphabetical position in the list
def totalNameScores(fileName):
	sortedNames = sorted(listOfNameValues(readFile(fileName)))
	finalScore = 0
	nameIndex = 0
	while nameIndex < len(sortedNames):
		finalScore += ((nameIndex + 1) * scoreName(sortedNames[nameIndex]))
		nameIndex += 1
	return finalScore

print(totalNameScores('p022_names.txt'))
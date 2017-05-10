# Names scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

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
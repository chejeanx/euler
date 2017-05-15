# Counting Sundays
# https://projecteuler.net/problem=19

# Returns if input year is a leap year
def isLeapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			return False
		return True

# Sets up calendar map with number of days per month
def calendarMap():
	calendar = {
		1: 31,
		2: 28,
		3: 31,
		4: 30,
		5: 31,
		6: 30,
		7: 31,
		8: 31,
		9: 30,
		10: 31,
		11: 30,
		12: 31
	}
	return calendar

# Figure out if a day a number of days from 1 Jan 1900 is a Sunday
def isSunday(numDaysFromSunday):
	return True if numDaysFromSunday % 7 == 0 else False

# Calculate number of Sundays that fall on first of month from 1 Jan of start year to 31 Dec of end year
def numSundaysOnFirstOfMonth(startYear, endYear):
	numDaysFromSunday = 1
	for year in range(1900, startYear):
		if isLeapYear(year):
			numDaysFromSunday += 366
		else:
			numDaysFromSunday += 365
	calendar = calendarMap()
	currentMonth = 1
	currentYear = startYear
	numSundaysOnFirst = 0
	while currentYear <= endYear:
		while currentMonth <= 12:
			if isSunday(numDaysFromSunday):
				numSundaysOnFirst += 1
			numDaysFromSunday += calendar[currentMonth]
			if isLeapYear(currentYear) and currentMonth == 2:
				numDaysFromSunday += 1
			currentMonth += 1
		currentMonth = 1
		currentYear += 1
	return numSundaysOnFirst

print(numSundaysOnFirstOfMonth(1901, 2000))
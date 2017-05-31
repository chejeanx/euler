# Coin sums
# https://projecteuler.net/problem=31

def numCoinCombos(total, coinValues):
	if total < 1:
		return int(total == 0)
	# if total == 0:
	# 	return 1
	# if total < 0:
	# 	return 0
	return sum(numCoinCombos(total - coinValues[i], coinValues[i:]) for i in range(len(coinValues)))

print(numCoinCombos(200, [1, 2, 5, 10, 20, 50, 100, 200]))
# Lattice paths
# https://projecteuler.net/problem=15

def numLatticePathsDP(x, y, width, height, latticeMap):
	if (x, y) == (width, height):
		return 1
	if (x, y) in latticeMap:
		return latticeMap[(x, y)]
	if x > width or y > height:
		return 0
	latticeMap[(x,y)] = numLatticePathsDP(x + 1, y, width, height, latticeMap) + numLatticePathsDP(x, y + 1, width, height, latticeMap)
	return latticeMap[(x, y)]

print(numLatticePathsDP(0, 0, 20, 20, {}))

def numLatticePathsRecursive(x, y, width, height):
	if (x, y) == (width, height):
		return 1
	if x > width or y > height:
		return 0
	return numLatticePathsRecursive(x + 1, y, width, height) + numLatticePathsRecursive(x, y + 1, width, height)

# print(numLatticePathsRecursive(0, 0, 20, 20))
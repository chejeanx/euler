# Integer right triangles
# https://projecteuler.net/problem=39

import math

# Returns perimeter less than or equal to n that has greatest number of possible right triangles
def rightTrianglePerim(n):
	triangles = {}
	for i in range(12, n + 1):
		for a in range(1, (i - 3) // 3 + 1):
			for b in range(a + 1, (i - a) // 2 + 1):
				c = i - a - b
				if c == math.sqrt(a**2 + b**2):
					if i not in triangles:
						triangles[i] = 1
					else:
						triangles[i] += 1

	return max(triangles, key = lambda i: triangles[i])

print(rightTrianglePerim(1000))
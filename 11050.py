m, n = map(int, input().split())

import math

def bino_coef_factorial(n, k):
	return math.factorial(n)//(math.factorial(n-k) * math.factorial(k))

print(bino_coef_factorial(m, n))
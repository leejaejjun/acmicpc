import math

N = int(input())
s, m ,l ,xl, xxl, xxxl = map(int, input().split())
T, p = map(int, input().split())

result = math.ceil(s / T)
result += math.ceil(m / T)
result += math.ceil(l / T)
result += math.ceil(xl / T)
result += math.ceil(xxl / T)
result += math.ceil(xxxl / T)

print(result)
print(N // p , N % p)
a, b = map(int, input().split())

def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

def max(m,n):
    i = 1
    while n*i % m != 0:
        i += 1 
    return n*i
print(gcd(a, b))
print(max(a,b))
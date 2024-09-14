import sys
input = sys.stdin.readline
N = int(input())
arr= []

for i in range(N):
    n = int(input())
    arr.append(n)

arr.sort()

for i in arr:
    print(i)
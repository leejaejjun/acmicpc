import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

arr = [i for i in range(1, N+1)]

q = deque(arr)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
    
print(q.popleft())
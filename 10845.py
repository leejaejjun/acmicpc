import sys
from collections import deque

input = sys.stdin.readline
d = deque([])

def push(deque, item):
    deque.append(item)

def pop(deque):
    if deque:
        return deque.popleft()
    return -1

def front(deque):
    if deque:
        return deque[0]
    return -1

def back(deque):
    if deque:
        return deque[-1]
    return -1

def size(deque):
    return len(deque)

def empty(deque):
    return 1 if not deque else 0

N = int(input())

for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        push(d, int(cmd[1]))
    elif cmd[0] == 'pop':
        print(pop(d))
    elif cmd[0] == 'size':
        print(size(d))
    elif cmd[0] == 'empty':
        print(empty(d))
    elif cmd[0] == 'front':
        print(front(d))
    elif cmd[0] == 'back':
        print(back(d))

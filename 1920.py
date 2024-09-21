import sys
input = sys.stdin.readline

# 첫 번째 입력: N개의 정수
N = int(input())
A = set(map(int, input().split()))  # 리스트를 set으로 변환하여 탐색 시간 단축

# 두 번째 입력: M개의 정수
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
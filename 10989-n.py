import sys

# 카운팅 정렬용 배열 생성 (숫자는 1 ~ 10000)
counts = [0] * 10001

# 입력을 빠르게 받아 처리
input = sys.stdin.read

# 입력된 모든 데이터를 가져와서 처리
data = input().splitlines()

N = int(data[0])

# 입력된 수를 카운트
for i in range(1, N + 1):
    counts[int(data[i])] += 1

# 결과를 출력 (한 번에 출력하여 메모리 절약)
output = sys.stdout.write
for num in range(1, 10001):
    if counts[num] > 0:
        output((str(num) + '\n') * counts[num])

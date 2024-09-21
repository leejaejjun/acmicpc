import sys
input = sys.stdin.readline

# 첫 번째 배열의 크기 읽기
N = int(input())
arr1 = list(map(int, input().strip().split()))

# 두 번째 배열의 크기 읽기
M = int(input())
arr2 = list(map(int, input().strip().split()))

# arr1의 요소 개수를 세기 위한 딕셔너리 생성
count_dict = {}
for num in arr1:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# arr2의 결과 준비
result = [count_dict.get(num, 0) for num in arr2]

# 결과를 한 줄로 출력
print(" ".join(map(str, result)))

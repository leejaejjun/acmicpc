N = int(input())
arr = list(map(int,input().split()))

count = 0

for i in arr:
    flag = False
    if  i==2:
        count +=1
        continue
    if i == 1:  # 1은 소수가 아님
        continue
    for k in range(2,i):
        if i % k == 0:
            flag = False
            break
        flag = True
    if flag == True:
        count+=1
print(count)

N = int(input())
for i in range(N):
    vps = input()
    count = 0
    for k in vps:
        if count < 0:
            break
        if k  == "(":
            count += 1
        else:
            count -= 1
        
    if count == 0:
        print("YES")
    else:
        print("NO")
        
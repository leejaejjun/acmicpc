a,b = map(int, (input().split()))

arr = []
brr = []
 
for i in range(a):
    tmp = input()
    arr.append(tmp)

    
for i in range(b):
    tmp = input()
    brr.append(tmp)

print(len(set(arr) & set(brr)))
for i in sorted(list(set(arr) & set(brr))):
    print(i)
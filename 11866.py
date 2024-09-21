N, n = map(int, input().split())

arr = [i+1 for i in range(N)]
arr_a = []
k = n - 1

while len(arr) != 1:
    
    arr_a.append(arr[k])
    del arr[k]
    k = ((k+n-1) % len(arr))
    
arr_a.append(arr[0])
print("<" + ", ".join(map(str, arr_a)) + ">")
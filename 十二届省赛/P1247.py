from functools import reduce
k = int(input())
arr = list(map(int,input().split()))
s = reduce(lambda x,y:x^y,arr)
ans = []
if s:
    for i in range(len(arr)):
        if arr[i]-(arr[i]^s)>0:
            print(arr[i]-(arr[i]^s),i+1)
            arr[i] = arr[i] ^s
            break
    print(*arr)
else:
    print("lose")

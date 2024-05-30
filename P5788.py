n=int(input())
arr=[0]+list(map(int,input().split()))
ans=[0]*(n+1)
stack=[]
for i in range(1,n+1):
    while len(stack) != 0 and arr[stack[-1]]<arr[i]:
        ans[stack.pop()]=i
    stack.append(i)
print(*ans[1:])

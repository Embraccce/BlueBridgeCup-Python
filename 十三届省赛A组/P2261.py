n,k=map(int,input().split())
ans = n*k
l=1
while l<=n:
    if k//l == 0:
        break
    r=min(n,n//(n//l))
    ans-=((l+r)*(r-l+1)//2)*(k//l)
    l=r+1
print(ans)

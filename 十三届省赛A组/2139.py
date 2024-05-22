n = int(input())
mod = 1000000007
ans = 0
l=1
def cal(l,r):
    return r*(r+1)*(2*r+1)//6-(l-1)*(l)*(2*l-1)//6
while l<=n:
    r=min(n,n//(n//l))
    ans+=(cal(l,r))*(n//l)
    l=r+1
print(ans%mod)

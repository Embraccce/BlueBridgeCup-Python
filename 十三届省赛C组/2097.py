n,x=map(int,input().split())
arr = [0]+list(map(int,input().split()))
presum=[0]*n
for i in range(1,n):
    presum[i] = presum[i-1]+arr[i]
def get_sum(l,r):
    return presum[r]-presum[l-1]
def check(y):
    for start in range(1,n-y+1):
        if get_sum(start,start+y-1)<2*x:
            return False
    return True
l=0
r=n+1
while l+1!=r:
    m = l+r>>1
    if not check(m):
        l = m
    else:
        r = m
print(r)

import os
import sys

# 请在此输入您的代码
n = int(input())
arr = [0]+list(map(int,input().split()))
# 预处理出前缀和数组
presum = [0] * (n+1)
m = int(input())
for i in range(1,n+1):
    presum[i] = presum[i-1]+arr[i]
def get_sum(l,r):
    return presum[r]-presum[l-1]
diff=[0]*(n+1)
cnt=[0]*(n+1)
sum1=0
sum2=0
for i in range(m):
    l,r=map(int,input().split())
    diff[l]+=1
    if r+1<=n:
        diff[r+1]-=1
    sum1+=get_sum(l,r)
# 重构出cnt数组
cnt[1] = diff[1]
for i in range(2,n+1):
    cnt[i] = cnt[i-1]+diff[i]
cnt = sorted(cnt[1:],reverse=True)
arr = sorted(arr[1:],reverse=True)
sum2=sum([cnt[idx] * arr[idx] for idx in range(n)])
print(sum2-sum1)

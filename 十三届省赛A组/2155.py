import os
import sys

# 13届省赛c题
n = int(input())
ans=0
i=2
while i*i<=n:
    if n%i==0:
        ans+=1
        while n%i==0:
            n=n//i
    i+=1
# 落单的算不出来！
if n>1:
    ans+=1
print(ans)

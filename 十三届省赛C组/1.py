import math
n = int(input())
mod = 998244353
a = (n*(n-1)//2)%mod
b = 1
for num in range(3,n+1):
    b = ((b%mod)*(num%mod))%mod
print((a*b)%mod)

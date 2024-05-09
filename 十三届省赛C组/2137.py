import math
import time
n = int(input())
start = time.time()
mod = 998244353
a = (n*(n-1)//2)%mod
b = (math.factorial(n)//2)%mod
print((a*b)%998244353)
end = time.time()
print(end-start)

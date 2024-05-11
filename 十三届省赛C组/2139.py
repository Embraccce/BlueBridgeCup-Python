import math
import time
n = int(input())
mod = 1000000007
def f(n):
    if n==1:
      return 1
    lst=set()
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            lst.add(i)
            lst.add(n//i)
    return sum([((num%mod)*(num%mod))%mod for num in lst])
def g(n):
    tot = 0
    for i in range(1,n+1):
        tot += f(i) % mod
    return tot
print(g(n)%mod)

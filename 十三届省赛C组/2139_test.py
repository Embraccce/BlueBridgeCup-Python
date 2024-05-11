import math
import time
sb = int(input())
mod = 1000000007
d=dict()
def f(n):
    global d
    if n==1:
        d[n**2]=d.get(n**2,0)+1
        return
    for i in range(1,math.ceil(math.sqrt(n))):
        if n % i == 0:
            d[i**2]=d.get(i**2,0)+1
            d[(n//i)**2]=d.get((n//i)**2,0)+1
    return
def g(n):
    tot = 0
    for i in range(1,n+1):
        f(i)
    for key,val in d.items():
        tot += key*val
    return tot
print(g(sb)%mod)

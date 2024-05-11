import math
n = int(input())
#mod = 10**9+7
mod = int(1e9)+7
def f(n):
    lst = []
    for i in range(1,math.ceil(math.sqrt(n))):
        lst.append(i)
        lst.append(n//i)
    return sum([num**2 for num in lst])
def g(n):
    tot = 0
    for i in range(1,n+1):
        tot += f(i) % mod
    return tot % mod
print(g(n))

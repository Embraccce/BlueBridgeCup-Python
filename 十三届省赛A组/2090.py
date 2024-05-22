import math
from collections import Counter
T=int(input())

prims = []
def prime(n):
    global prims
    vis = [False] * (n+1)
    for i in range(2,n+1):
        if not vis[i]:prims.append(i)
        j=0
        while i*prims[j] <= n:
            vis[i*prims[j]] = True
            if i % prims[j] ==0:break
            j+=1
    return

def is_perfect_square(n):
    return round(math.sqrt(n))**2 == n

def is_prefect_cube(n):
    return round(n ** (1. / 3)) ** 3 == n

def process(ai):
    global prims
    if is_perfect_square(ai) or is_prefect_cube(ai):
        return True
    for num in prims:
        if ai % num == 0:
            cnt=0
            while ai % num == 0:
                ai//=num
                cnt+=1
            if cnt==1:
                return False
        if ai<num:
            break
    if is_perfect_square(ai) or is_prefect_cube(ai):
        return True

    return False

prime(4000)
for _ in range(T):
    ai = int(input())
    if process(ai):
        print("yes")
    else:
        print("no")

        
        
        

n = int(input())
import math
for _ in range(n):
    a,b,c,d,k=map(int,input().split())
    ans=0
    for x in range(a,b+1):
        for y in range(c, d+1):
            if math.gcd(x,y)==k:
                ans+=1
    print(ans)

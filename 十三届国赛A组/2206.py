T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    s = set()
    for x in range(1, m+1):
        if n % x in s:
            print("Yes")
            break
        else:
            s.add(n % x)
    else:
        print("No")

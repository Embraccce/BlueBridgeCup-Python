T = int(input())
for i in range(T):
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = [0 for _ in range(N)]
    for k in range(N-1):
        b[k] = a[N-k-1]-a[N-k-2]-1
    b[N-1] = a[0] - 1
    s=0
    for k in range(0,len(b),2):
        s^=b[k]
    if s:
        print("Georgia will win")
    else:
        print("Bob will win")

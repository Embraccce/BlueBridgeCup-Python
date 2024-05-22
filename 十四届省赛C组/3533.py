n,m = map(int,input().split())
d = [[0 for i in range(n+2)] for i in range(n+2)]
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    d[x1][y1]+=1
    d[x2+1][y1]-=1
    d[x1][y2+1]-=1
    d[x2+1][y2+1]+=1
a = [[0 for i in range(n+2)] for i in range(n+2)]
for i in range(1,n+1):
    for j in range(1,n+1):
        a[i][j] = a[i-1][j]+a[i][j-1]-a[i-1][j-1]+d[i][j]
        print(a[i][j]%2,end="")
    print()

import copy
n,m=map(int,input().split())
f = [[float('inf')]*(n) for i in range(n)]
# 设置自身到自身的距离为0
for i in range(n):
    f[i][i] = 0
for _ in range(m):
    u,v,w=map(int,input().split())
    f[u-1][v-1] = f[v-1][u-1] = min(w,f[v-1][u-1])
for k in range(n):
    for i in range(n):
        for j in range(n):
            f[i][j] = min(f[i][k]+f[k][j],f[i][j])
for i in range(n):print(*f[i])

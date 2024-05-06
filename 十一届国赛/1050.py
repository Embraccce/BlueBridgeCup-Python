import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
n,D = map(int,input().split())
points = []
for i in range(n):
    x,y = map(int,input().split())
    points.append([x,y])

# 构建领接矩阵
f = [[0]*n for i in range(n)]
for i in range(len(f)):
    for j in range(i+1, len(f)):
        dis = distance(points[i][0],points[i][1],points[j][0],points[j][1])
        if dis > D:
            f[j][i] = f[i][j] = float('inf')
        else:
            f[j][i] = f[i][j] = dis

del points

#Floyd
for k in range(len(f)):
    for i in range(len(f)):
        for j in range(len(f)):
            f[i][j] = min(f[i][j],f[i][k]+f[k][j])

dp=[[float('inf')] * n for i in range(1<<n)]
dp[1][0]=0

for s in range(1<<n):
    for i in range(n):
        # i要在集合s中
        if (s & (1<<i)):
            for j in range(n):
                # j != i and j要在集合s中
                if j != i and (s & (1<<j)):
                # 去掉i
                    dp[s][i] = min(dp[s][i],dp[s^(1<<i)][j] + f[j][i])

ans = float('inf')
# 最后还要回到原点
for i in range(n):
    ans = min(ans,dp[(1<<n)-1][i]+f[i][0]) 
print(f"{ans:.2f}")

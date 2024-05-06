import math
n = 21
g = [[float('inf')]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if math.gcd(i+1,j+1) == 1:
            g[i][j] = 0
dp=[[0]*n for i in range(1<<n)]
dp[1][0] = 1
for s in range(1<<n):
    for i in range(n):
        if s & (1<<i):
            for j in range(n):
                if s & (1<<j) and g[j][i] == 0:
                    dp[s][i] += dp[s^(1<<i)][j]
print(sum(dp[(1<<n)-1]))

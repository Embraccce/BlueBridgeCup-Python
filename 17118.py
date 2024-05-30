N = int(input())
H = []
for i in range(N):
    H.append(list(map(int,input().split())))
dp = [[float('inf') for i in range(N)] for i in range(N)]
dp[0][0] = 0
for r in range(N):
    for c in range(N):
        if r + 1 < N:
            dp[r+1][c] = min(dp[r][c]+1,dp[r+1][c])
        if c + 1 < N:
            dp[r][c+1] = min(dp[r][c]+1,dp[r][c+1])
        if c+1>N-1 or H[r][c] <= H[r][c+1]:
            continue
        else:
            for L in range(1,N-c):
                if H[r][c+L-1] > H[r][c+L]:dp[r][c+L] = min(dp[r][c]+1,dp[r][c+L])
                else:break
print(dp[-1][-1])

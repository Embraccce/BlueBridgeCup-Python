N = int(input())
arr = [[0]*N for i in range(N)]
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(i+1):
        arr[i][j] = temp[j]

dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][0][0] = arr[0][0]

for i in range(1, N):
    for j in range(i+1):
        # 左上
        if 0 <= i-1 <= N-1 and 0 <= j - 1 <=N-1:
            dp[i][j][0] = dp[i-1][j-1][0]+arr[i][j]
            dp[i][j][1] = dp[i-1][j-1][1]
            dp[i][j][2] = dp[i-1][j-1][2] + 1
        # 右上
        if 0 <= i-1 <= N-1 and 0 <= j <=N-1:
            if dp[i-1][j][0]+arr[i][j] > dp[i][j][0]:
                dp[i][j][0] = dp[i-1][j][0]+arr[i][j]
                dp[i][j][1] = dp[i-1][j][1] + 1
                dp[i][j][2] = dp[i-1][j][2]

ans = 0
for pos in dp[-1]:
    now,x,y = pos
    if abs(x-y)<=1:
        ans = max(ans,now)
print(ans)

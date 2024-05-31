import os
import sys

# 请在此输入您的代码
ans = 0
def dfs(nownum, posx, posy, vis, ans, idx):
    if nownum == 16:
        ans[idx] += 1
        return
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = posx + dx, posy + dy
        if 0 <= new_x < 4 and 0 <= new_y < 4 and vis[new_x][new_y] == 0:
            vis[new_x][new_y] = 1
            dfs(nownum + 1, new_x, new_y, vis, ans, idx)
            vis[new_x][new_y] = 0  # 回溯


vis = [[0] * 4 for i in range(4)]
# 开始搜索
cnt = 0
ans = [0 for i in range(17)]  # 用列表存储结果以便传递引用
for i in range(4):
    for j in range(4):
        vis[i][j] = 1
        dfs(1, i, j, vis, ans,i+1)
        vis[i][j] = 0
print(vis)
print(sum(ans))

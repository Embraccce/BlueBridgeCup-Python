cur_x,cur_y,cur_dir=0,0,0
ans = [[0]*100 for i in range(100)]
ans[0][0] = 1
for num in range(2, 1000):
    if cur_dir == 0:
        cur_y += 1
        cur_dir = 1
    elif cur_dir == 1:
        cur_x += 1
        cur_y -= 1
        if cur_y == 0:
            cur_dir = 2
    elif cur_dir == 2:
        cur_x += 1
        cur_dir = 3
    elif cur_dir == 3:
        cur_x -= 1
        cur_y += 1
        if cur_x == 0:
            cur_dir = 0
    ans[cur_x][cur_y] = num
print(ans[19][19])

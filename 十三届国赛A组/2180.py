import string
import bisect
s=list(input())
mp = {i:[] for i in string.ascii_lowercase}
for idx in range(len(s)):
    mp[s[idx]].append(idx)
m = int(input())
for _ in range(m):
    l,r,x,y = input().split()
    l,r=map(int,[l,r])
    x_l = bisect.bisect_left(mp[x],l-1)
    x_r = bisect.bisect_right(mp[x],r-1)
    mp[x].sort()
    # mp[y]添加
    mp[y].extend(mp[x][x_l:x_r])
    # 字符串s对应的位置修改为y
    for idx in mp[x][x_l:x_r]:
        s[idx] = y
    # mp[x]删除
    del mp[x][x_l:x_r]
print("".join(s))


##s=input()
##m=int(input())
##for _ in range(m):
##    l,r,x,y = input().split()
##    l,r=map(int,[l,r])
##    if x in s[l-1:r]:
##        s=s[:l-1]+s[l-1:r].replace(x,y)+s[r:]
##print(s)

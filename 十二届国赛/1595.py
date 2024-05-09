n = int(input())
arr = [0] + list(map(int,input().split()))
tot = arr.copy()
dot = arr.copy()
dot[0] = 1
pos = [0]
for i in range(1,n+1):
    tot[i] += tot[i-1]
    dot[i] *= dot[i-1]
    if arr[i]!=1:
        pos.append(i)
# 防止最后一位是1，这样无法找到正确的二分位置
if arr[-1] == 1:
    pos.append(n+1)
def check(l, r):
    return (dot[r] // dot[l-1]) - (tot[r] - tot[l-1])
ans = 0
for L in range(1,n+1):
    for idx in range(1,len(pos)):
        if L > pos[idx]:
            continue
        else:
            # 二分查找
            l,r = pos[idx-1],pos[idx]
            while l+1!=r:
                m = l+r>>1
                if check(L,m)>=0:
                    l = m
                else:
                    r = m
            # 防止中间没有夹数字，以及确保找到了
            if pos[idx-1]<l<pos[idx] and check(L,l) == 0:
                ans+=1
                
            # 查找不是连续的1
            if pos[idx] != n+1:
                res = check(L,pos[idx])
                if res == 0:
                    ans+=1
                elif res > 4e10:
                    break
print(ans)

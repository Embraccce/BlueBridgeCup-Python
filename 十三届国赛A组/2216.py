import sys
n,m,jb=map(int,input().split())
books = {idx:num for idx, num in enumerate(map(int, input().split()),start=1)}
record = {i:[] for i in range(1,n+1)}
for _ in range(m):
    b,l,r = map(int,input().split())
    record[b].append((l,r))
res=0
ans=[]
for book in range(1,n+1):
    record[book].sort(key=lambda x:(x[0],x[1]))
    # 对book进行操作:
    arr = record[book]
    tmp=[]
    while len(arr) != 0:
        del_list = []
        x,y=arr[0]
        l=1
        idx=1
        del_list.append(0)
        while idx<len(arr):
            if record[book][idx][0] > y:
                x,y = record[book][idx]
                l += 1
                del_list.append(idx)
            idx += 1
        tmp.append(l)
        for index in sorted(del_list, reverse=True):
            del arr[index]
    res += sum(tmp[:books[book]])
    ans.extend(tmp[books[book]:])
ans.sort(reverse=True)
print(res+sum(ans[0:jb]))

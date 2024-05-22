n=int(input())
d=dict()
for i in range(n):
    a,b = map(int,input().split())
    if a in d.keys():
        d[a].append(b)
        d[a].sort()
    else:
        d[a] = [b]
ans = 0
for key,value in d.items():
    if len(value) == n // 10:
        continue
    elif len(value) > (n // 10):
        ans += sum(d[key][:(len(value)-(n // 10))])
print(ans)
        
        
        

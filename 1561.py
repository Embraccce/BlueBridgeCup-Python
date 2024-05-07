import sys
n = 20210605
# Eluer筛
vis = set()
prim = []
for i in range(2, n+1):
    if i not in vis:
        prim.append(i)
    j = 0
    while i * prim[j] <= n:
        vis.add(i * prim[j])
        if i % prim[j] == 0:
            break
        j += 1


ans = 0
for num in prim:
    for bit in str(num):
        if bit not in ['2','3','5','7']:
            ans += 1
            break
print(len(prim)-ans)

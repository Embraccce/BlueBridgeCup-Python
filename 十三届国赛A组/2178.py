import os
import sys

# 请在此输入您的代码
import copy
n,Q=map(int,input().split())
D=[]
L=[]
for _ in range(n):
    D.append(list(map(int,input().split())))
for _ in range(n):
    L.append(list(map(int,input().split())))

def get_sum(m):
    return sum([sum(row) for row in m])

def floyd(m):
    # 初始化, Floyd求最短路
    for k in range(len(m)):
        for i in range(len(m)):
            for j in range(i+1, len(m)):
                m[i][j] = min(m[i][j], m[i][k]+m[k][j])
                m[j][i] = m[i][j]
    return m

def sub(day):
    # 首先减去k轮
    k = day // n
    r = day % n
    t = copy.deepcopy(D)
    for i in range(n):
        for j in range(i+1,n):
            t[i][j] = max(L[i][j], t[i][j]-2*k)
            t[j][i] = t[i][j]
    # 然后减去剩下的
    for city in range(r):
        for i in range(n):
            if i != city:
                t[city][i] = max(L[city][i], t[city][i]-1)
                t[i][city] = t[city][i]
    t = floyd(t)
    return t
# 初始化的dis
dis = floyd(copy.deepcopy(D))
if get_sum(dis) <= Q:
    print(0)
elif get_sum(floyd(copy.deepcopy(L))) > Q:
    print(-1)
else:
    l,r=0,100000
    while l+1!=r:
        m = (l + r) // 2
        if get_sum(sub(m)) > Q:
            l = m
        else:
            r = m
    print(r)

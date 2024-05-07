import math
def lcm(a,b):
    return a*b//math.gcd(a,b)

n = 2021
g = [[float('inf')]*n for _ in range(n)]
for a in range(n):
    for b in range(n):
        if abs(a-b) <= 21:
            g[a][b] = g[b][a] = lcm(a+1,b+1)
        if a == b:
            g[a][b] = 0

# floyd求最短路径
def floyd(g):
    dist = g[:]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

#dijkstra求最短路径
def dijkstra(n, src):
    dist = [float('inf')]*n
    vis = [False]*n
    dist[src] = 0

    # 找最短的加入到S中：
    for _ in range(n):
        # 待加入的点为u
        u, min_dist = min([(i, dist[i]) for i in range(n) if not vis[i]], key=lambda x: x[1])
        vis[u] = True
        for v in range(n):
            if not vis[v]:
                dist[v] = min(dist[v],dist[u] + g[u][v])
    return dist

print(dijkstra(n,0)[-1])


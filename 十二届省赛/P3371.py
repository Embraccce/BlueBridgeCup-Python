import sys
inf = (1<<31)-1
def dijkstra(n, src):
    dist = [inf]*n
    vis = [False]*n
    dist[src] = 0

    # 找最短的加入到S中：
    for _ in range(n):
        # 待加入的点为u
        u, min_dist = min([(i, dist[i]) for i in range(n) if not vis[i]], key=lambda x: x[1])
        vis[u] = True
        for v in range(n):
            if not vis[v]:
                dist[v] = min(dist[v],dist[u] + g.get((u,v),inf))
    return dist

n, m, s = map(int, input().split())
g = dict()

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    g[(u-1,v-1)] = min(g.get((u-1,v-1),inf), w)
ans = dijkstra(n, s-1)
sys.stdout.write(" ".join(map(str, (ans[i] for i in range(n)))))

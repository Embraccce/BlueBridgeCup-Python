import itertools
near = {
        "a":["b","f"],
        "b":["a","g","c"],
        "c":["b","d","g"],
        "d":["c","e"],
        "e":["d","g","f"],
        "f":["a","g","e"],
        "g":["f","b","e","c"],

    }


def DFS(near, start, vis):
    vis.add(start)
    for neighbour in near[start]:
        if neighbour not in vis:
            DFS(near, neighbour, vis)


def check(edges):
    sub = {edge:near[edge] for edge in edges}
    for edge in sub:
        sub[edge] = [neighbour for neighbour in sub[edge] if neighbour in edges]
    vis = set()
    DFS(sub, edges[0], vis)
    return vis == set(edges)


ans = 0
for num in range(1,8):
    for choice in itertools.combinations("abcdefg",num):
        if check(choice):
            ans += 1
print(ans)



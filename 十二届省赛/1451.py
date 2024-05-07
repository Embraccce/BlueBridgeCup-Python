N = int(input())
tree = {i:[] for i in range(1,N+1)}
for idx,i in enumerate(range(N-1),start=2):
    tree[int(input())].append(idx)

def dfs(node):
    if len(tree[node]) == 0:
        return 0
    maxn = 0
    for sub_node in tree[node]:
        maxn=max(maxn,dfs(sub_node))

    print(len(tree[node]),maxn)
    return len(tree[node]) + maxn
    # 同一级的首位相连，加这一级有个最长的“节外生枝”的长度
print(dfs(1))

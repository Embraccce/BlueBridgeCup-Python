import sys
sys.setrecursionlimit(100000)         #设置最大递归深度
n = int(input())
A = [[] for i in range(n + 1)]          #根是从索引1开始,所以索引0就不用了,开n加1个位置

#构建二叉树存储输入的值
for i in range(2, n + 1):
    v = int(input())                      #相当于是第v层有i,i+1,i+2....这几个节点
    A[v].append(i)                        #把节点加到输入的那一层中去

#深度优先搜索与动态规划
def dfs(i):
    if A[i] is None:                      #叶子节点,高度为0
        return 0

    maxn = 0
    print(A[i])
    for j in A[i]:                     #以i为父节点的所有子节点的二叉树的高度最大值
        maxn = max(maxn, dfs(j))            #以i为节点形成的所有二叉树的高度最大值

    return len(A[i]) + maxn               #孩子节点的个数 + 以孩子节点为根节点构成二叉树的高度最大值

dfs(1)          #以1作为根节点二叉树的最高的高度

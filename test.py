def multi(A, B, mod=int(1e9+7)):
    m,n,p = len(A),len(A[0]),len(B[0])
    ret = [[0]*p for i in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                ret[i][j] = (ret[i][j] + A[i][k] * B[k][j] % mod) % mod
    return ret

def fastPowMatrix(A, n, mod=int(1e9+7)):
    N = len(A)
    ret = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while n:
        if n & 1:
            ret = multi(ret, A, mod)
        A = multi(A, A, mod)
        n >>= 1
    return ret

n,k = map(int,input().split())
A = []
for i in range(n):
    temp = list(map(int,input().split()))
    A.append(temp)

    
ans = fastPowMatrix(A, k)


for i in range(n):
    print(*ans[i],sep=" ")

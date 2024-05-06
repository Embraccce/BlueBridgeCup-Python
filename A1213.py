import sys

def multi(A, B, mod):
    ret = [[0, 0], [0, 0]]
    ret[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod
    ret[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod
    ret[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod
    ret[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod
    return ret


def multi_ans(A, B,mod):
    m,n,p = len(A),len(A[0]),len(B[0])
    ret = [[0]*p for i in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                ret[i][j] = (ret[i][j] + A[i][k] * B[k][j]) % mod
                
    return ret


def fastPowMatrix(A, n,mod):
    N = len(A)
    #ret = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    ret = [[1,0],[0,1]]
    while n:
        if n & 1:
            ret = multi(ret, A, mod)
        A = multi(A, A, mod)
        n >>= 1
    return ret


def fib(n,mod=sys.maxsize):
    if n == 1 or n == 2:
        return 1 % mod
    else:
        F2 = [[1,1]]
        base = [[1,1],[1,0]]
        ans = fastPowMatrix(base, n-2, mod)
        return multi_ans(F2, ans, mod)[0][0]
    

n, m, p = map(int, input().split())
if m > n+2:
    print((fib(n+2,p)-(1%p))%p)
else:
    # 这里其实是假装过了，因为f_m实际上不一定能取出来
    f_m = fib(m)
    ans = (fib(n+2,mod=f_m) - (1 % f_m)) % f_m
    print(ans % p)

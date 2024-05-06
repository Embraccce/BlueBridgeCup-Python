import sys
import time
def multi(A, B, mod=int(1e9+7)):
    #m,n,p = len(A),len(A[0]),len(B[0])
    ret = [[0, 0], [0, 0]]
    ret[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod
    ret[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod
    ret[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod
    ret[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod
    return ret


def multi_ans(A, B, mod=int(1e9+7)):
    m,n,p = len(A),len(A[0]),len(B[0])
    ret = [[0]*p for i in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                ret[i][j] = (ret[i][j] + A[i][k] * B[k][j]) % mod
    return ret


def fastPowMatrix(A, n, mod=int(1e9+7)):
    N = len(A)
    #ret = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    ret = [[1,0],[0,1]]
    while n:
        if n & 1:
            ret = multi(ret, A, mod)
        A = multi(A, A, mod)
        n >>= 1
    return ret


n = int(input())
start_time = time.time()
base = [[1,1],[1,0]]
F2 = [[1,1]]

ans = fastPowMatrix(base, n-2)
if n==1 or n==2:
    print(1)
else:
    print(multi_ans(F2, ans)[0][0])
end_time = time.time()
# 计算时间差（单位：秒）
execution_time = end_time - start_time

print("代码执行时间为:", execution_time, "秒")

n = int(input())
A,B,C = list(map(int,input().split())),list(map(int,input().split())),list(map(int,input().split()))
def check(arr):
    cnt, tot = 0, 0
    for num in arr:
        tot += num
        if tot <= 0:
            break
        else:
            cnt+=1
    return cnt

ans = max([check(sorted([A[i]-B[i]-C[i] for i in range(n)],reverse=True)),check(sorted([B[i]-A[i]-C[i] for i in range(n)],reverse=True)),check(sorted([C[i]-A[i]-B[i] for i in range(n)],reverse=True))])
if ans==0:
    print(-1)
else:
    print(ans)

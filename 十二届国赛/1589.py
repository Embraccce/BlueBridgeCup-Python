n,m = map(int,input().split())
s = [0] + [1 if ch == "(" else -1 for ch in input()]
for _ in range(m):
    op = list(map(int,input().split()))
    if len(op) == 3:
        for idx in range(op[1],op[2]+1):
            s[idx] *= -1
    else:
        tot = s[op[1]]
        r = 0
        for i in range(op[1]+1,n+1):
            if tot < 0:
                break
            tot += s[i]
            if tot == 0:
                r=i
        print(r)

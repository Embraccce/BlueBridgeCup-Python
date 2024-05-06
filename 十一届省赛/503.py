N = int(input())
lines = set()
for i in range(N):
    A,B = map(int,input().split())
    lines.add((A,B))
lines = list(lines)
def cal(line,cur):
    intersection = []
    a2,b2 = line
    for a1,b1 in cur:
        if a1 == a2:
            continue
        x = (b2-b1) / (a1-a2)
        y = (a1*b2-a2*b1) / (a1-a2)
        if (x,y) not in intersection:
            intersection.append((x,y))
    return len(intersection)
ans = 2
for i in range(1, len(lines)):
    ans += (1+cal(lines[i],lines[:i]))
print(ans)

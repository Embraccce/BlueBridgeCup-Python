S = input()
T = input()
n,m = len(S),len(T)
def check2(s,t):
    map1 = {}
    map2 = {}
    for a, b in zip(s, t):
        if a in map1:
            if map1[a] != b:
                return False
        else:
            map1[a] = b
    return True
def check(k):
    trans = dict()
    for i in range(n):
        for j in range(m):
            s = S[i:i+k]
            t = T[j:j+k]
            if len(s) == k and len(t) == k:
                if check2(s,t):return True
    return False
l,r=0,min(n,m)+1
while l+1!=r:
    m = (l+r)//2
    if check(m):
        l = m
    else:
        r = m
print(l)

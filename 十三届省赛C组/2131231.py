t = int(input())
def check6(a,b,c):
    if a+b==c or a+c==b or b+c==a:
        return True
    elif a==b or a==c or b ==c:
        return True
    else:
        return False
def check4(a1,b1,a2,b2,a3,b3):
    for i in [a1,b1]:
        if i == a2+a3 and b2 == b3:
            return True
        elif i == a2 + b3 and b2 == a3:
            return True
        elif i == b2 + a3 and a2 ==b3:
            return True
        elif i == b2 + b3 and a2 == a3:
            return True
        elif i ==a2 and a2 ==a3:#三条边相等,4种
            return True
        elif i ==a2 and a2 ==b3:
            return True
        elif i ==b2 and b2 == a3:
            return True
        elif i == b2 and b2 == b3:
            return True

for i in range(t):
    s = list(map(int,input().split()))
    ans = 8#因为边数有3这种情况，4（完美，有两边加起来等于另一边，另一边刚刚好相等，6（有两边加起来等于另一边，8（每个边都不等，任意两边加起来也不等第三边，
    a1,b1,a2,b2,a3,b3 = s[0],s[1],s[2],s[3],s[4],s[5]
    for i in range(0,2):
        for j in range(2,4):
            for k in range(4,6):
                x1,x2,x3 = s[i],s[j],s[k]
                if check6(x1,x2,x3):
                    ans = min(6,ans)
                if check4(a1,b1,a2,b2,a3,b3):
                    ans = min(4,ans)
                if check4(a2,b2,a1,b1,a3,b3):
                    ans = min(4,ans)
                if check4(a3,b3,a1,b1,a2,b2):
                    ans = min(4,ans)
    print(ans)

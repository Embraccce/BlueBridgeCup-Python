T=int(input())
for _ in range(T):
    a1,b1,a2,b2,a3,b3 = map(int,input().split())
    rect=[[0,0],[a1,b1],[a2,b2],[a3,b3]]
    comb = ((1,2),(1,3),(2,3))
    check = []
    for r1,r2 in comb:
        common = list(set(rect[r1]) & set(rect[r2]))
        if len(common) == 1:
            lst1 = rect[r1].copy()
            lst1.remove(common[0])
            lst2 = rect[r2].copy()
            lst2.remove(common[0])
            check.append((r1,r2,common[0],lst1[0] + lst2[0]))
        elif len(common) == 2:
            check.append((r1,r2,common[0],2*common[1]))
            check.append((r1,r2,common[1],2*common[0]))
    if len(check)==0:
        for r1,r2 in comb:
            r3=6-r1-r2
            x1,y1=rect[r1]
            x2,y2=rect[r2]
            if x1+x2 in rect[r3] or x1+y2 in rect[r3] or y1+x2 in rect[r3] or y1+y2 in rect[r3]:
                print(6)
                break
        else:
            print(8)
    else:
        for i in check:
            r3 = 6-i[0]-i[1]
            if len(set(i[2:]) & set(rect[r3]))!=0:
                print(4)
                break
        else:
            print(6)
                

import math
fx = {
    0:(-1,0),
    1:(-0.5,math.sqrt(3)/2),
    2:(0.5,math.sqrt(3)/2),
    3:(1,0),
    4:(0.5,-math.sqrt(3)/2),
    5:(-0.5,-math.sqrt(3)/2)
}
d1,p1,q1,d2,p2,q2=map(int,input().split())
x1=y1=x2=y2=0
x1+=fx[d1][0]*p1+fx[(d1+2)%6][0]*q1
y1+=fx[d1][1]*p1+fx[(d1+2)%6][1]*q1
x2+=fx[d2][0]*p2+fx[(d2+2)%6][0]*q2
y2+=fx[d2][1]*p2+fx[(d2+2)%6][1]*q2
dis = (x1-x2)**2+(y1-y2)**2
if math.sqrt(dis) == int(math.sqrt(dis)):
    print(int(math.sqrt(dis)))
else:
    dx=abs(x1-x2)
    dy=abs(y1-y2)
    ans = 0
    if (dx/0.5) > (dy/(math.sqrt(3)/2)):
        step_y = round(dy/(math.sqrt(3)/2))
        step_x = round(dx - step_y*0.5)
        ans += step_x + step_y
    else:
        step_x = round(dx/0.5)
        step_y = round((dy - step_x*(math.sqrt(3)/2))/ math.sqrt(3)*2)
        ans += step_x + step_y
    print(ans)

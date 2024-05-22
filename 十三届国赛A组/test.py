s=input()
m=int(input())
for _ in range(m):
    l,r,x,y = input().split()
    l,r=map(int,[l,r])
    if x in s[l-1:r]:
        s=s[:l-1]+s[l-1:r].replace(x,y)+s[r:]
print(s)

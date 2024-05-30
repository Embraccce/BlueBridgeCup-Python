n,q=map(int,input().split())
c = [0]*(n+1)
def modify(x,y,z):
    if x > n or x < 1:return
    c[x] = z  
    if y <= 0:
      return
    modify(x//2,y-1,z)
    modify(2*x,y-1,z)
    modify(2*x+1,y-1,z)
for _ in range(q):
    query = list(map(int,input().split()))
    if len(query) == 4:
        x,y,z=query[1:]
        modify(x,min(y,40),z)
    else:
        print(c[query[1]])

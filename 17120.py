from queue import PriorityQueue
h1 = PriorityQueue()
h2 = PriorityQueue()
n,p,q=map(int,input().split())
A = [0] + list(map(int,input().split()))
A = A[:p]+sorted(A[p:q+1])+A[q+1:]
ans = A[q] - A[p]
for i in range(p,q+1):
    h1.put(A[i])
    h2.put(-A[i])
num_min,num_max = A[p],A[q]
for i in range(q+1,n+1):
    h1.put(A[i])
    h2.put(-A[i])
    num_min = h1.get()
    h2.get()
    num_max = -h2.get()
    h2.put(-num_max)
    ans = max(ans,num_max-num_min)
h1 = PriorityQueue()
h2 = PriorityQueue()
for i in range(p,q+1):
    h1.put(A[i])
    h2.put(-A[i])
for i in range(p-1,0,-1):
    h1.put(A[i])
    h2.put(-A[i])
    num_max = -h2.get()
    h1.get()
    num_min = h1.get()
    h1.put(num_min)
    ans = max(ans,num_max-num_min)
print(ans)

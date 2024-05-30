n=int(input())
A = [0]+list(map(int,input().split()))
left=[0]*(n+1)
right=[n+1]*(n+1)
ans=0
st=[]
for i in range(1,n+1):
    while len(st) != 0 and A[st[-1]]>A[i]:
        right[st.pop()]=i
    st.append(i)
st.clear()
for i in range(n,0,-1):
    while len(st) != 0 and A[st[-1]]>A[i]:
        left[st.pop()]=i
    st.append(i)
for i in range(1,n+1):
    ans = max(ans, (right[i]-left[i]-1)*A[i])
print(ans)

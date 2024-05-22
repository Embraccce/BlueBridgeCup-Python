n,x=map(int,input().split())
S=sorted(input())
if S[0]!=S[x-1]:
  print(S[x-1])
elif S[x]==S[-1]:
  print(''.join(S[::x]))
else:
  print(''.join(S[x-1:]))

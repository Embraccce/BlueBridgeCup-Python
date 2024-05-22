n=int(input())
for _ in range(n):
    T = list(input())
    S = list(input())
    ans=0
    for j in range(1,len(S)-1):
        if S[j]==T[j]:
            continue
        elif S[j-1]==S[j+1] and S[j]!=S[j+1]:
            S[j]=S[j+1]
            ans+=1
    if S == T:
        print(ans)
    else:
        print(-1)

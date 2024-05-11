ans = [[1189,841]]
for i in range(1,10):
    ans.append(sorted((max(ans[-1])//2,min(ans[-1])),reverse=True))
print(*ans[int(input()[1:])],sep="\n")

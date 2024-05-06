s = list(input())
m = sorted(sorted(s),key=s.count,reverse=True)[0]
print(m,s.count(m),sep="\n")

lst=((9,9),(9,6),(9,5),(10,3),(10,1),(10,2))
ans = sorted(lst,key=lambda x:(-x[0], x[1]))
print(ans)

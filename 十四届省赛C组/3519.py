s = input()
ans = 0
i = 0
while i < len(s)-1:
    if s[i]==s[i+1] or s[i] == "?" or s[i+1] == "?":
        i += 1
        ans += 1
    i += 1
print(ans)

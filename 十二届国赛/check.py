def check(s):
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == "(" * mid and s[mid:] == ")" * mid
    
print(check("())("))
print(check("((("))
print(check("())"))
s = list(input().split())
print(s)
print("".join(s))

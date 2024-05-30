n,m = map(int,input().split())
mod = 998244353
ans = 0
def is_odd(n):
    return (n & 1) == 1

def is_even(n):
    return (n & 1) == 0


def check1(num):
    s=str(num)[::-1]
    if is_odd(len(s)):
        s = s + "0"
    for idx in range(0,len(s),2):
        if is_odd(int(s[idx])) and is_even(int(s[idx+1])):
            continue
        else:
            return False
    return True

def check2(num,m):
    s=str(num)
    for idx in range(0,len(s)-4):
        if sum(map(int,s[idx:idx+5])) > m:
            return False
    return True
        
for num in range(10**(n-1), 10**(n)):
    if check1(num) and check2(num,m):
        ans += 1
print(ans % 998244353)

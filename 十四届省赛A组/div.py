def div(num1,num2):
    num1 = list(map(int,num1))
    r = 0
    ans = []
    for i in range(len(num1)):
        r = r * 10 + num1[i]
        ans.append(r//num2)
        r %= num2
    ans = "".join(map(str,ans)).lstrip("0")
    return ans if ans else "0"
num1=input().strip()
num2=int(input().strip())
print(div(num1,num2))

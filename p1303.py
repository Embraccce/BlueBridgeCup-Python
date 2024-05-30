a=input().strip()
b=input().strip()
def mul(num1,num2):
    if num1 == "0" * len(num1) or num2 =="0" * len(num2):
        return "0"
    ret = [0]*(len(num1)+len(num2)+1)
    num1 = list(map(int,list(num1)))[::-1]
    num2 = list(map(int,list(num2)))[::-1]
    for i in range(len(num1)):
        for j in range(len(num2)):
            ret[i+j]+=num1[i]*num2[j]
            ret[i+j+1]+=ret[i+j]//10
            ret[i+j]%=10
    return "".join(map(str,ret[::-1])).lstrip("0")
print(mul(a,b))


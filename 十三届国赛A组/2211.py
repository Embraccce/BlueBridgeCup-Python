import time
from sys import stdout,stdin

def sub(num1,num2):
    l = len(num2)
    ans = []
    num1=list(map(int,num1))[::-1]
    num2=([0]+list(map(int,num2)))[::-1]
    for i in range(l+1):
        if num1[i] < num2[i]:
            num1[i+1]-=1
            num1[i]+=10
        ans.append(num1[i]-num2[i])
    num1 = ans+num1[l+1:]
    del num2,ans
    return "".join(map(str,num1))[::-1]
def add(num1, num2):
    l = len(num2)
    num1 = list(map(int,num1))[::-1]
    num2 = ([0]+list(map(int,num2)))[::-1]
    carry = 0
    ans = []
    for i in range(l+1):
        tot = num1[i]+num2[i]+carry
        ans.append(tot%10)
        carry = tot // 10
    ans.append(num1[l+1]+carry)
    num1 = ans + num1[l+2:]
    del ans, num2
    return "".join(map(str,num1[::-1]))

def div(num1,num2):
    num1 = list(map(int,num1))
    r=0
    ans=[]
    for i in range(len(num1)):
       r=r*10+num1[i]
       ans.append(r//num2)
       r%=num2
    del num1
    print = stdout.write
    flag = 0  
    for num in ans[1:]:
        print(num.__str__())
    

n = int(input())
n1="40"*(n)+"0"
n2="8"*(n)+"0"
a = sub(n1,n2)
del n1,n2
a = add(a,str(4*n))
div(a,9)

def cmp(num1, num2):
    if len(num1) != len(num2):
        return len(num1) > len(num2)
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            return num1[i] > num2[i]
    return True

def sub(num1, num2):
    if cmp(num1, num2):
        sign = ""
        n1, n2 = num1, num2
    else:
        sign = "-"
        n1, n2 = num2, num1

    # 小的数左边补0
    n2 = n2.zfill(len(n1))

    # 转换为列表以便修改
    n1 = list(n1[::-1])
    n2 = list(n2[::-1])

    ret = []

    for i in range(len(n1)):
        if int(n1[i]) < int(n2[i]):
            n1[i + 1] = str(int(n1[i + 1]) - 1)
            n1[i] = str(int(n1[i]) + 10)
        ret.append(str(int(n1[i]) - int(n2[i])))

    res = ''.join(ret[::-1]).lstrip('0')
    return (sign + res) if res else "0"

# 输入处理
num1 = input().strip()
num2 = input().strip()

# 计算结果
ans = sub(num1, num2)

# 输出结果
print(ans)
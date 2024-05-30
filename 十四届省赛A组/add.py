def add(num1, num2):
    max_len = max(len(num1),len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    # 反转字符串，以便从最低位开始相加
    num1 = num1[::-1]
    num2 = num2[::-1]

    carry = 0
    ret = []

    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i])

        tot = int(num1[i]) + int(num2[i]) + carry
        carry = tot // 10
        ret.append(str(tot % 10))

    if carry:
        ret.append(str(carry))

    return ''.join(ret[::-1])

num1 = input()
num2 = input()
print(add(num1, num2))

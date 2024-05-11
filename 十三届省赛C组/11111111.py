# 打开两个文件
with open('out.txt', 'r') as file1, open('myout.txt', 'r') as file2:
    # 逐行读取并比较
    for i, (line1, line2) in enumerate(zip(file1, file2), start=1):
        # 如果内容不同
        if line1 != line2:
            # 打印出行号和内容
            print(f"Difference at line {i}:")
            print("ans: ", line1)
            print("my_ans: ", line2)

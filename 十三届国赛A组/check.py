import timeit

# 测试使用 append 方法逐个添加元素
def test_append():
    arr = []
    for i in range(1000):
        arr.append(i)

# 测试使用 extend 方法一次性添加所有元素
def test_extend():
    arr = []
    arr.extend(range(1000))

# 测量执行时间
append_time = timeit.timeit(test_append, number=10000)
extend_time = timeit.timeit(test_extend, number=10000)

print(f"使用 append 方法的执行时间: {append_time:.6f} 秒")
print(f"使用 extend 方法的执行时间: {extend_time:.6f} 秒")

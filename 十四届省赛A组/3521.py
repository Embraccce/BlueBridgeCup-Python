from collections import deque
class MonotonicQueue:
    def __init__(self, compare):
        self.mp = deque()
        self.compare = compare

    def push(self, value):
        while self.mp and self.compare(self.mp[-1], value):
            self.mp.pop()
        self.mp.append(value)

    def front(self):
        return self.mp[0]

    def pop(self, value):
        if self.mp and self.mp[0] == value:
            self.mp.popleft()

n, m, a, b = map(int, input().split())
mod = 998244353
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def solve(compare):
    m = []
    ret = []
    # 求每行
    for row in arr:
        mq = MonotonicQueue(compare)
        ans = []
        for i in range(len(row)):
            # 移除生命周期到了的队头元素
            if i >= b:
                mq.pop(row[i - b])
            mq.push(row[i])
            if i >= b - 1:
                ans.append(mq.front())
        m.append(ans)

    # 转置一下求每列
    m = list(zip(*m))
    for row in m:
        mq = MonotonicQueue(compare)
        for i in range(len(row)):
            # 移除生命周期到了的队头元素
            if i >= a:
                mq.pop(row[i - a])
            mq.push(row[i])
            if i >= a - 1:
                ret.append(mq.front())
    return ret

ans_max = solve(lambda x, y: x < y)
ans_min = solve(lambda x, y: x > y)
print(sum([(ans_min[i] * ans_max[i]) % mod for i in range(len(ans_min))]) % mod)

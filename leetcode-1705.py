import queue
import sys
q = queue.PriorityQueue()
ans=0
apples =[20000]
days=[20000]
for d in range(len(apples)+max(days)):
    if d < len(apples) and apples[d] != 0 and days[d] != 0:
        q.put([d + days[d], apples[d]])

    # 清理过期的苹果和数量为0的苹果
    while not q.empty():
        time, count = q.get()
        if d < time and count > 0:
            q.put([time, count])
            break

    # 吃苹果
    if not q.empty():
        ans += 1
        time, count = q.get()
        q.put([time, count-1])
print(ans)

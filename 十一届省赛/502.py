total = int(input())
tg = 0
yx = 0
for i in range(total):
    score = int(input())
    if score >= 60:
        tg += 1
    if score >= 85:
        yx += 1
print(f"{tg/total*100:.0f}%")
print(f"{yx/total*100:.0f}%")

lines = set()

def check(point,cur):
    global line
    x1,y1 = point
    for x2,y2 in cur:
        if x1 == x2:
            k,b = float('inf'),x1
        else: 
            k,b = (y2-y1)/(x2-x1),(x2*y1-x1*y2)/(x2-x1)
        lines.add((k,b))

cur = []
for x in range(0,20):
    for y in range(0,21):
        cur.append((x,y))

for x in range(0,20):
    for y in range(0,21):
        check((x,y),list(set(cur)-set((x,y))))
print(len(lines))

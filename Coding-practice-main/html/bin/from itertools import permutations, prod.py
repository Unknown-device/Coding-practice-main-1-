from itertools import permutations, product
from collections import Counter, deque

COLORS = list('RG')
colorcount = len(set(COLORS))
TEXT = "Some random text for trying out    oottmmmeeerr"
TEXT = "DIE SONNE SOLL DIR IMMER SCHEINEN"
# TEXT = "hello there"
#TEXT = 'abc'
freq = Counter(TEXT)

print(freq)

count = 1
q = deque()
stop = False
uniq_chars = len(freq.keys())
#print(f"uniq {uniq_chars}")
while True:
    for p in product(COLORS, repeat=count):
        #print(f"perm - {p}")
        prefix = p[:-1]
        if prefix:
            if prefix in q:
                q.remove(prefix)
            #print(f"{p}, prefix: {prefix}")
        if not p in q:
            q.append(p)
        if len(q) == uniq_chars:
            #print("reached count")
            stop = True
            break
    if not stop:
        q.popleft()
        count += 1
        if count <= colorcount: continue
        COLORS = COLORS + [COLORS[len(COLORS)% colorcount]]
        print("new colors : ", COLORS)
    else:
        break   

t = 0
for item, val in zip(q, sorted(freq.values(), reverse=True)):
    print(item, val, val*len(item))
    t += val*len(item)
#print(len(q))
print(t) 

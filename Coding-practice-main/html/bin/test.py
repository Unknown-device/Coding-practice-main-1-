from itertools import product
from collections import Counter, deque

COLORS = list('RB')
colorcount = len(set(COLORS))
TEXT = "DIE SONNE SOLL DIR IMMER SCHEINEN"
freq = Counter(TEXT) 

print("Character Frequencies:", freq)

count = 1
q = deque()
stop = False
uniq_chars = len(freq.keys())

while True:
    for p in product(COLORS, repeat=count):
        prefix = p[:-1]
        if prefix:
            if prefix in q:
                q.remove(prefix)
        q.append(p)
        if len(q) == uniq_chars:
            stop = True
            break
            
    if not stop:
        q.popleft()
        count += 1
        if count <= colorcount: continue
        COLORS = COLORS + [COLORS[len(COLORS)% colorcount]]
    else:
        break   


sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) 

t = 0
for i, (item, (char, freq_val)) in enumerate(zip(q, sorted_freq)):
    print(f"Permutation: {item}, Character: '{char}', Frequency: {freq_val}, Product: {freq_val * len(item)}")
    t += freq_val * len(item)


encrypted_result = ""
text_length = len(TEXT)

for i in range(text_length):
    encrypted_result += TEXT[i % len(TEXT)]  

print(f"Encrypted result: {encrypted_result}")

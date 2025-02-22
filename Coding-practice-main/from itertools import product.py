from itertools import product
from collections import Counter, deque

COLORS = list('RB')
colorcount = len(set(COLORS))
TEXT = "DIE SONNE SOLL DIR IMMER SCHEINEN"
freq = Counter(TEXT)  # Now spaces will also be counted

print("Character Frequencies:", freq)

count = 1
q = deque()
stop = False
uniq_chars = len(freq.keys())

# Generate color permutations until we have enough
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

# Now, we'll add the unique letters based on their frequency
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)  # Sorting characters by frequency

t = 0
for i, (item, (char, freq_val)) in enumerate(zip(q, sorted_freq)):
    print(f"Permutation: {item}, Character: '{char}', Frequency: {freq_val}, Product: {freq_val * len(item)}")
    t += freq_val * len(item)

# Generate encrypted result (mapping of TEXT to permutations)
encrypted_result = ""
text_length = len(TEXT)

# Loop to map every character from TEXT to a color permutation
for i in range(text_length):
    encrypted_result += TEXT[i % len(TEXT)]  # Ensure this loops through TEXT for full coverage

print(f"Encrypted result: {encrypted_result}")

# Decryption: Map color permutations back to the original characters
decrypted_result = ""
sorted_freq_dict = dict(sorted_freq)

# Reverse the mapping: Assign each permutation back to the character based on its frequency
for i, item in enumerate(q):
    char = list(sorted_freq_dict.keys())[i]  # Get the character corresponding to the frequency order
    decrypted_result += char

# Ensure the decrypted result is the same length as the original text
decrypted_result = decrypted_result[:text_length]  # Slice to match the original length

print(f"Decrypted result: {decrypted_result}")

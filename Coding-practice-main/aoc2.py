
with open("C:\\Users\\hadi\\Downloads\\aoc\\Aoc2input.txt") as f:
    s = f.read()
s = s.splitlines()

report = 0

for i in range(len(s)):
    s[i] = s[i].split()
print(s)
for j in range(len(s)):    
    v = [int(s[0][i+1])-int(s[0][i]) for i in range(len(s[0])-1)]
    for k in range(len(v)):
        if v[k] < 3 and v[k] > 0:
            safe = True
        else:
            safe = False
if safe == True:
    report += 1
print(report)
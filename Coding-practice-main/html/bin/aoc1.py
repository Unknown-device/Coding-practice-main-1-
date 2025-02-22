with open("C:\\Users\\hadi\\Downloads\\aoc\\Aoc1input.txt") as f:
    s = f.read()
leftlist = []
rightlist = []
s = s.splitlines() 
for i in range(len(s)):
    rightlist.append(s[i].split()[0])
    leftlist.append(s[i].split()[1])
leftlist.sort()
rightlist.sort()
distance = 0


for i in range(len(leftlist)):
    distance += abs(int(leftlist[i]) - int(rightlist[i]))
print(distance)
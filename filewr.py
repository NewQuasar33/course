l = []
f = []
z =str()
with open('qwerty.txt') as inf:
    line = inf.readline()
    line = line.strip()
for i in range(len(line)):
    if line[i] >= 'A':
        l += line[i]
    elif line[i] < 'A' and line[i-1] <'A':
        continue
    elif line[i] < 'A':
        z = line[i]
        if line[((i+1) % len(line))] < 'A':
            z += line[i+1]
        f += [z]
ouf = open('text.txt', 'w')
for i in range(len(l)):
    ouf.write(l[i] * int(f[i]))
ouf.close()
name = []
math = []
ph = []
lg = []
middle = []
i = 0
middlemath = 0
middleph = 0
middlelg = 0
with open('dataset_3363_4.txt') as inf:
    for line in inf:
        a, b, c, d = line.strip().split(';')
        name.append(a)
        math.append(int(b))
        ph.append(int(c))
        lg.append(int(d))
for i in range(len(name)):
    middle.append((math[i] + ph[i]+ lg[i])/3)
    middlemath += math[i]
    middleph += ph[i]
    middlelg += lg[i]
middlemath = middlemath/len(name)
middleph = middleph/len(name)
middlelg = middlelg/len(name)
print(middlemath, end=' ')
print(middleph, end=' ')
print(middlelg, end=' ')
print(middle)
ouf = open('text.txt', 'w')
for i in range(len(name)):
    ouf.write(str(middle[i]) + '\n')
ouf.write(str(middlemath) + ' ' )
ouf.write(str(middleph) + ' ')
ouf.write(str(middlelg) )
ouf.close()
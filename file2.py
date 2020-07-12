with open('dataset_3363_3.txt') as inf:
    l = inf.read().lower().split()
maxC = 0
maxI = 0
for i in range(len(l)):
    if l.count(l[i]) == maxC:
        if l[i] < l[maxI]:
            maxC = l.count(l[i])
            maxI = i
    elif l.count(l[i]) > maxC:
        maxC = l.count(l[i])
        maxI = i
print(l[maxI], maxC)
ouf = open('text.txt', 'w')
ouf.write(str(l[maxI]))
ouf.write(' ')
ouf.write(str(maxC))
ouf.close()
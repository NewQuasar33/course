a = [int(i) for i in input().split()]
b = list()
for i in range(len(a)):
    if a.count(a[i]) > 1 and a[i] not in b:
        b.append(a[i])
for j in range(len(b)):
    print(b[j], end=' ')
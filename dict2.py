a = [i for i in input().lower().split()]
b = list()
for i in range(len(a)):
    if a[i] not in b:
        print(a[i], a.count(a[i]))
        b.append(a[i])
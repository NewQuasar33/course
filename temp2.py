a = 0
lst = []
lb = []
while 1 == 1:
    a = input()
    if a == 'end':
        break
    else:
        a = a.split()
        lst +=[ [a[i] for i in range(len(a))]] #считали массив
        lb +=[[0 for i in range(len(a))]]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        for di in range(-1, 2):
            ai = i + di
            lb[i][j] += int(lst[(ai)%len(lst)][j])
        for dj in range(-1, 2):
            aj = j + dj
            lb[i][j] += int(lst[ai][(aj)%len(lst(i))])
for i in range(len(lst)):
    for j in range(len(lb[i])):
        print(lb[i][j], end=' ')
    print()
#print(lst)
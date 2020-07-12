a = [int(i) for i in input().split()]
s = 0
for i in range(len(a)):
    if len(a) == 1:
        print(a[i])
    else:
        s = a[i-1] + a [(i+1)% len(a)]
        print(s, end=' ')
c, d, a, b = int(input()), int(input()), int(input()), int(input())
for i in range(a, b+1):
    print('\t', i, end='')
for i in range(c, d+1):
    print()
    print(i, end='\t')
    for j in range(a, b+1):
        print(j * i, end='\t')
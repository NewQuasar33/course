n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = i, j
        print(a[i][j], end='\t')
    print()
n = int(input())
dic = {}
a =[]
for i in range(n):
    a += [int(input())] #считали список
for j in range(len(a)):
    if a[j] not in dic:
        dic[a[j]] = f(a[j])
        print(dic[a[j]])
    else:
        print(dic[a[j]])
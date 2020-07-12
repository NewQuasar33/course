dic = {}
k = 1
v = -1
def update_dictionary(d, key, value):
    key = int(key)
    if key in d:
        d[key] += [value]
    elif 2*key in d:
        d[2*key] += [value]
    else:
        d[2*key] = [value]
update_dictionary(dic, k, -1)
print(dic)
update_dictionary(dic, 2, -2)
print(dic)
update_dictionary(dic, 1, -3)
print(dic)
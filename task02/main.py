def swap(l):
    length = len(l)
    for i in range(0, length, 2):
        if i < length - 1:
            tmp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = tmp
    return l

lst = input("Введите список через пробел")
a = lst.split()
print(str(swap(a)))
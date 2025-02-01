lst = []
lst2 = []

j = 0
with open("webpage.txt", "r", encoding="gbk") as file:
    for i in file.readlines():
        if j % 2:
            lst2.append(i)
        else:
            lst.append(i)
        j += 1

print("let lst =", lst)
print("let lst2 =", lst2)

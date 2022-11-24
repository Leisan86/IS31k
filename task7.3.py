a = input("Введите строку для проверки: ")
b = input("Введите проверочную строку: ")
count = 0
i = 1
while i != -1:
    i = a.find(b)
    if i >= 0:
        count += 1
    a = a[i+1:]

print(count)
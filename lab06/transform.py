text = input("Введите целые числа одной строкой: ")

original = []
for token in text.split():
    original.append(int(token))


transformed = []
for x in original:
    if x < 0:
        transformed.append(-x)
    else:
        transformed.append(x)

print(f"Исходный список: {original}")
print(f"Новый список: {transformed}")

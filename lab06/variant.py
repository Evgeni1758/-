text = input("Введите целые числа одной строкой: ")


numbers = []
for token in text.split():
    numbers.append(int(token))


selected = []
for x in numbers:
    if abs(x) > 5:
        selected.append(x)


count = len(selected)
total = 0
for x in selected:
    total = total + x


sorted_copy = sorted(selected)


print(f"Выборка: {selected}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Отсортированная копия: {sorted_copy}")

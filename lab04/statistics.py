n = int(input("Сколько чисел будет введено: "))

# Первое число вводим отдельно — им же инициализируем максимум
first = int(input("Число 1: "))
total = first
positives = 0
maximum = first

if first > 0:
    positives = positives + 1

for i in range(2, n + 1):
    x = int(input(f"Число {i}: "))
    total = total + x
    if x > 0:
        positives = positives + 1
    if x > maximum:
        maximum = x

print(f"Сумма: {total}")
print(f"Положительных: {positives}")
print(f"Максимум: {maximum}")

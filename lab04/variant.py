n = int(input("Сколько чисел будет введено (n >= 0): "))

count = 0
total = 0

for i in range(1, n + 1):
    x = int(input(f"Число {i}: "))
    if 10 <= x <= 20:
        count = count + 1
        total = total + x

print(f"Количество: {count}")
print(f"Сумма: {total}")

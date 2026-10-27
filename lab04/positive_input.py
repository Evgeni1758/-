rejected = 0
x = int(input("Введите целое число: "))

while x <= 0:
    rejected = rejected + 1
    x = int(input("Число не положительное, попробуйте ещё раз: "))

print(f"Квадрат числа: {x * x}")
print(f"Отклонённых попыток: {rejected}")

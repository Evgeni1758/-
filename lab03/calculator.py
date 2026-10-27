num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))
op = input("Операция (+, -, *, /): ")

if op == "+":
    result = num1 + num2
    print(f"Результат: {result:.2f}")
elif op == "-":
    result = num1 - num2
    print(f"Результат: {result:.2f}")
elif op == "*":
    result = num1 * num2
    print(f"Результат: {result:.2f}")
elif op == "/":
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = num1 / num2
        print(f"Результат: {result:.2f}")
else:
    print("Неизвестная операция")

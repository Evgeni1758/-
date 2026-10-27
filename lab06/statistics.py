text = input("Введите целые числа одной строкой: ")

numbers = []
for token in text.split():
    numbers.append(int(token))

if len(numbers) == 0:
    print("Нет данных")
else:
    count = len(numbers)

    total = 0
    for x in numbers:
        total = total + x

    
    minimum = numbers[0]
    maximum = numbers[0]
    for x in numbers:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x

    average = total / count

    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")

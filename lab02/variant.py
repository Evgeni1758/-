# Ввод общего объёма и вместимости одной единицы
total = int(input("Количество фотографий: "))
capacity = int(input("Фотографий на странице: "))

# Расчёты
full_units = total // capacity          # полностью заполненные страницы
remainder = total % capacity            # остаток фотографий
min_units = (total + capacity - 1) // capacity  # минимальное число страниц

# Вывод
print(f"Полностью заполненных страниц: {full_units}")
print(f"Остаток фотографий: {remainder}")
print(f"Минимальное число страниц: {min_units}")

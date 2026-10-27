# Запрос названий предметов
subject1 = input("Название первого предмета: ")
subject2 = input("Название второго предмета: ")

# Запрос количества занятий по каждому предмету за неделю
count1 = int(input(f"Количество занятий по предмету '{subject1}' за неделю: "))
count2 = int(input(f"Количество занятий по предмету '{subject2}' за неделю: "))

# Запрос продолжительности одного занятия в минутах
duration1 = int(input(f"Продолжительность одного занятия по предмету '{subject1}' (мин): "))
duration2 = int(input(f"Продолжительность одного занятия по предмету '{subject2}' (мин): "))

# Запрос доступного времени на неделю в часах
available_hours = float(input("Доступное время на неделю (часы): "))

# Расчёт нагрузки в минутах для каждого предмета
load1 = count1 * duration1
load2 = count2 * duration2

# Общая нагрузка в минутах и часах
total_minutes = load1 + load2
total_hours = total_minutes / 60

# Остаток свободного времени в часах
free_hours = available_hours - total_hours

# Нагрузка за четыре одинаковые недели (в часах)
four_weeks_hours = total_hours * 4

# Вывод результатов
print(f"\nНагрузка по предмету '{subject1}': {load1} мин")
print(f"Нагрузка по предмету '{subject2}': {load2} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {four_weeks_hours:.2f} ч")

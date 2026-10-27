# profile.py

# Запрос данных
surname = input("Введите фамилию: ")
name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст (целое от 1 до 120): "))
subject = input("Введите любимый предмет: ")
hours = float(input("Введите количество часов подготовки в неделю: "))

# Вычисления
full_name = f"{name} {surname}"
age_in_4_years = age + 4
hours_for_4_weeks = hours * 4
average_hours_per_day = hours / 7

# Вывод карточки
print("\n" + "=" * 40)
print("              КАРТОЧКА")
print("=" * 40)
print(f"Фамилия:              {surname}")
print(f"Имя:                  {name}")
print(f"Полное имя:           {full_name}")
print(f"Группа:               {group}")
print(f"Город:                {city}")
print(f"Возраст:              {age} лет")
print(f"Возраст через 4 года: {age_in_4_years} лет")
print(f"Любимый предмет:      {subject}")
print(f"Часов в неделю:       {hours:.2f}")
print(f"За 4 недели:          {hours_for_4_weeks:.2f} ч")
print(f"В среднем в день:     {average_hours_per_day:.2f} ч")
print("=" * 40)

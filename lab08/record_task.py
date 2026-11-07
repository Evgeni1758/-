# record_task.py

# Создаем словарь с ключами title и hours
course = {
    "title": "Python для начинающих",
    "hours": 40
}

# Изменяем hours и добавляем completed = False
course["hours"] = 48
course["completed"] = False

print("Итоговый словарь:", course)

# Создаем кортеж из title и hours
course_pair = (course["title"], course["hours"])

# Распаковываем его в две переменные
title, hours = course_pair

print(f"Название: {title}")
print(f"Часы: {hours}")
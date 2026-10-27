# Запрос названия заказа и имени заказчика
order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

# Первая позиция
item1_name = input("Название первой позиции: ")
item1_qty = int(input(f"Количество '{item1_name}': "))
item1_price = float(input(f"Цена единицы '{item1_name}' (руб): "))

# Вторая позиция
item2_name = input("Название второй позиции: ")
item2_qty = int(input(f"Количество '{item2_name}': "))
item2_price = float(input(f"Цена единицы '{item2_name}' (руб): "))

# Доставка и внесённая сумма
delivery = float(input("Стоимость доставки (руб): "))
paid = float(input("Внесённая сумма (руб): "))

# Расчёты
item1_cost = item1_qty * item1_price
item2_cost = item2_qty * item2_price
goods_total = item1_cost + item2_cost
grand_total = goods_total + delivery
total_qty = item1_qty + item2_qty
change = paid - grand_total

# Вывод
print()
print("=== ЗАКАЗ:", order_name, "===")
print("Заказчик:", customer_name)
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {item2_cost:.2f}")
print(f"Стоимость товаров без доставки: {goods_total:.2f} руб")
print(f"Стоимость доставки: {delivery:.2f} руб")
print(f"Общая сумма с доставкой: {grand_total:.2f} руб")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб")



my_records = [
        {"title": "Хлеб",              "category": "продукты",      "amount": 45},
        {"title": "Молоко",            "category": "продукты",      "amount": 89},
        {"title": "Сыр",               "category": "продукты",      "amount": 320},
        {"title": "Стиральный порошок","category": "бытовая химия", "amount": 410},
        {"title": "Мыло",              "category": "бытовая химия", "amount": 60},
        {"title": "Наушники",          "category": "техника",       "amount": 2500},
    ]
    
print("Список покупок:")
for r in my_records:
        print(f"  - {r['title']} ({r['category']}): {r['amount']} руб.")
        
    
print(f"Общая стоимость всех покупок: {total_amount(my_records)} руб.")
    
print("\nСтоимость по категориям:")
for cat, amount in by_category(my_records).items():
        print(f"  {cat}: {amount} руб.")
        
print(f"\nСписок покупок по алфавиту: {titles_sorted(my_records)}")
    
expensive = most_expensive(my_records)
print(f"Самая дорогая покупка: {expensive['title']} за {expensive['amount']} руб.")
text = input("Введите строку: ")

count = 0

for word in text.split():
    cleaned = word.strip(".,!?;:").lower()
    if cleaned == "":
        continue
    if len(cleaned) >= 5:
        print(cleaned)
        count = count + 1

if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")

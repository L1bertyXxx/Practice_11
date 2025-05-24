import csv

file = "products.csv"
sum = 0

print("Нужно купить:")
with open(file, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["Продукт"]
        quantity = int(row["Количество"])
        price = int(row["Цена"])
        sum += quantity * price
        print(f"{product} - {quantity} шт. за {price} руб.")

print(f"Итоговая сумма: {sum} руб.")
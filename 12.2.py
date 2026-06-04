import json

shop = {"products": [
{
    "name": "Шоколад",
    "price": 50,
    "available": True,
    "weight": 100
},
{
    "name": "Кофе",
    "price": 100,
    "available": False,
    "weight": 250
},
{
    "name": "Чай",
    "price": 70,
    "available": True,
    "weight": 50
}
]}

with open("Продукты.json", 'w', encoding="utf-8") as file:
    json.dump(shop, file, ensure_ascii=False, indent=2)

print("Новые товары")

count = int(input("Сколько добавляем? "))

with open("Продукты.json", 'r', encoding="utf-8") as file:
    data = json.load(file)

for i in range(count):
    print(f"Товар {i + 1}:")

    name = input("Название товара: ")
    price = int(input("Цена: "))
    weight = int(input("Вес: "))

    available_input = input("Есть в наличии? (да/нет): ").lower()
    if available_input == "да":
        available = True
    else:
        available = False

    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

    data["products"].append(new_product)
    print(f"Товар {name} добавлен!")

with open("Продукты.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print()
print("Список товаров:")

with open("Продукты.json", 'r', encoding="utf-8") as file:
    data = json.load(file)

    for p in data["products"]:
        print(f"Название: {p['name']}")
        print(f"Цена: {p['price']}")
        print(f"Вес: {p['weight']}")

        if p["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

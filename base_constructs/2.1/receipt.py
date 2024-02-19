## Формат ввода
# * название товара;
# * цена товара;
# * вес товара;
# * количество денег у пользователя.
## Формат вывода
# Чек
# <название товара> - <вес>кг - <цена>руб/кг
# Итого: <итоговая стоимость>руб
# Внесено: <количество денег от пользователя>руб
# Сдача: <сдача>руб

product_name = input()
product_price = int(input())
product_weight = int(input())
user_cash = int(input())
print("Чек")
print(f"{product_name} - {product_weight}кг - {product_price}руб/кг")
print(f"Итого: {product_price * product_weight}руб")
print(f"Внесено: {user_cash}руб")
print(f"Сдача: {user_cash - product_price * product_weight}руб")

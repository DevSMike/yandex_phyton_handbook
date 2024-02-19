## Формат ввода
# Три натуральных числа:
# * цена товара;
# * вес товара;
# * количество денег у пользователя.
## Формат вывода
# Одно целое число — сдача, которую требуется отдать пользователю

product_price = int(input())
product_weight = int(input())
user_cash = int(input())
print(user_cash - product_price * product_weight)
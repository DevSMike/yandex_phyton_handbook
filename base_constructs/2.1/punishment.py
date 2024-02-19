## Формат ввода
# В первой строке записано одно натуральное число N
# Во второй строке записана часть наказания.
#
##  Формат вывода
# N строк вида: Я больше никогда не буду писать "<часть наказания>"!

str_number = int(input())
str_punishment = input()
str_result_punishment = "Я больше никогда не буду писать \"" + str_punishment + "\"!"
print(str_number * (str_result_punishment + "\n"))
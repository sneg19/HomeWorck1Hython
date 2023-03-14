## Задача 2: Найдите сумму цифр трехзначного числа.

## Пример:

## 123 -> 6 (1 + 2 + 3)
## 100 -> 1 (1 + 0 + 0) |

## Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного


number = int(input("Введите трехзначное число: "))


number_1 = number % 10
number_2 = (number // 10) % 10
number_3 = number // 100

resoult_number = number_1 + number_2 + number_3

print(resoult_number)
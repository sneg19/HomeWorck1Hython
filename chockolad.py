#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no

lenght = int(input("Введите длину плитки: "))

width = int(input("Введите ширину плитки: "))

result = int(input("Сколько плиток Вы хотите отломить? "))

square_chockolad = lenght * width

if result < square_chockolad and (result % lenght == 0 or result % width == 0):
    print("Возможно")
else:
    print("Не возможно")
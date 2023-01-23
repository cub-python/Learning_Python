'''
Числа и типы чисел.
Числа в языке Python представлены тремя встроенными типами:
целые (int), вещественные (float) и комплексные (comlex),
а так же двумя типами чисел, которые предоставляет его стандартная
библиотека: десятичные дроби
неограниченной точности (Decimal)
и обыкновенные дроби (Float).
функция;
- float() число с плавающей точкой
- окргуление int()
- модул math
- sqrt() - выводит корень из числа
и другие в разных местах
'''

# Задача.1 float, int

num1 = float(input('Введите вешественное число: '))
num2 = float(input('Введите вешественное число: '))
# sum = (num1 + num2)
print(num1 + num2)
sum = (num1 + num2)
print(int(sum))  # int переобразует веществ число в целое


# Задача.2
# f - math,это библиотекаБ разные работы с числами
import math

# num = input('Vvedite chislo: ')
# koren = math.sqrt(float(num))
# print('Корень из числа:', '%.2f' % koren)


# Задача.3
'''
User vedet 3 veshestvennoe chislo, poschitat summu 
'''
# a
num1 = float(input('Введите вешественное число: '))
num2 = float(input('Введите вешественное число: '))
num3 = float(input('Введите вешественное число: '))
sum = num1 + num2 + num3

print('Summa 3x chisel: ', '%.2f' % sum)
# b
# Написать программу которя попросит Юзера вести 2 числа
# и посчитает сумму чему равен корени и квадрат,
# Корень числа ",,,," квадрат числа "...."

num1 = int(input('Vedite celoe czislo: '))
num2 = int(input('Vedite celoe czislo: '))
korenb1 = math.sqrt(num1)
korenb2 = math.sqrt(num2)

print('Koren iz czisel: ',  '%.2f' % korenb1,  '%.2f' % korenb2)

sum_korenb = korenb1 + korenb2
print('Summa kornei: ', '%.2f' % sum_korenb)

kvadrat_czisel = (num1**2, num2**2)
print('Kvadraty czisel: ', kvadrat_czisel)

print('Korenb iz czisel: ', '%.2f' % korenb1,  '%.2f' % korenb2,','
      'kvadrat czisel: ', kvadrat_czisel)

# Zadacza 4
'''
Naiti dlinu okruzhnosti(O). esli znaesh ploshadb(S)
formula :O = korenb\S4p
math.pi = 3.14
'''
s_okr = float(input('Введите площадь окружности: ', ))
l_okr = math.sqrt(s_okr*4*math.pi)
print('Длина окружности равен: ', '%.2f' %l_okr)





# Zadacha 5
'''
Masteru nuzhno nitka dlinoi 50 sm, chtoby kroit kraya izdelya
Napisatb programmu chtob naiti skolbko ne hvataet
U kvadrata 4 storony
'''
treb = 50.0
s_plosh1 = float(input('Введите площадь: '))
s_plosh2 = float(input('Введите площадь: '))

len1 = math.sqrt(s_plosh1)*4 # из s_plosh1 выведим корень и умножим 4(сторона)
len2 = math.sqrt(s_plosh2)*4 # из s_plosh1 выведим корень и умножим 4(сторона)
len = len1 + len2
tr_len = (50 - len)

print('Не хватает:','%.2f' %tr_len, 'sm')


# Zadacha 6
#
num = float(input('Введите число: '))
print('Корень числа: ', num, '-', 'равен', '%.2f' %math.sqrt(num), 'а квадрат числа равен: ', num **2)


# Задача 7
'''
найти результат выражеения |a| + |b|
Значения переменных a b поступают на вход в отдельных строках
и могут быть только целого типа
'''
a = int(input(Введите целое число можно и отриц))





































'''
'''
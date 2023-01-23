'''
Okruglenie chisel do 2 i 3 razryada posle zapyatoi
'''
# Zadacha 8
# num = float(input('Введите вещественное число: '))
# print(round(num, 2), round(num, 3))  #round okruglyaet nam do nuzhogo parametra
#
#

# Zadacha 9. Raznostb vremen
'''
Данные значения двух моментов. Тут нам надо перевести всё в секунды
1 nour = 3600 sek, 1 min = 60
'''

hour1 = int(input('Введите часы(целые числа): '))
min1 = int(input('Введите минуту(целые числа): '))
sek1 = int(input('Введите секунда (целые числа): '))
#
hour2 = int(input('Введите часы(целые числа): '))
min2 = int(input('Введите часы(целые числа): '))
sek2 = int(input('Введите часы(целые числа): '))

data1 = (hour1 * 3600) + (min1 * 60) + sek1

data2 = (hour2 * 3600) + (min2 * 60) + sek2

difference = data1 - data2
print(abs(difference))

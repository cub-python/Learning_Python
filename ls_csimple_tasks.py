# запрвашивать у пользователя 3 числа и выводит сумму? произв, вычитание чисел
# Zadacha.1
# num1 = int(input('Vvedite pervoe chislo: ', ))
# num2 = int(input('Vvedite pervoe vtoroe: ', ))
# num3 = int(input('Vvedite pervoe chislo: ', ))
# # summa_chisel = print('Summa chisel: ', num1 + num2 + num3)
#
# sum = (num1 + num2 + num3)
# print('Summa chisel: ', + sum)
# multiplication = (num1 * num2 * num3)
# print('Полчаемое число: ', multiplication)
#
# division = (num1 / num2 / num3)
# print('При вычитание получаем: ', division) # esli tut dobavit '% 2.f'
# print('Средне арифметическое число: ', '%.2f' % (sum / 2)) # esli tut dobavit '%.2f'

# Zadacha №2
'''3 друзья собираются на шашлыки треб сумма 15000, выводит кто сколько ввел
и уточнить скольо не хватает
'''

# trebsumma = int(15000)
# friend1 = int(input('Skolko deneg u tebya:', ))
# friend2 = int(input('Skolko deneg u tebya:', ))
# friend3 = int(input('Skolko deneg u tebya:', ))
#
# sum = friend1 + friend2 + friend3
# print(sum)
#
# itog = trebsumma - sum
# print('Не хватает: ', itog, 'руб')
#
# # Zadacha №3
'''
Узнать у юзера чему равно числа х и у,посчитать,чему равно 3х^2+2ху-6у^2
'''

x = int(input('Chemu ravno x?:', ))
y = int(input('Chemu ravno y?:', ))
rez1 = ((3 * x * x) + (2 * x * y) - (6 * y * y))
print('3х^2+2ху-6у^2 = ', rez1)
# Цикл  for
# Есть ли в тексте буква "ы"?,found -нашли? letter -буква, word-слово? break- остановка цикла
# lower ()-это встроенный метод, используемый для обработки строк.
# Методы lower () возвращают строку в нижнем регистре из заданной строки.
# Он преобразует все заглавные символы в строчные.

# found = False

word = input('Введите слово:').lower()
for letter in word:
    if letter == 'ы' or letter == 'Ы':
        found = True

if found:
    print('Есть')
else:
    print('Нет')


# Программа сравнивает посл  букву,если нет то предпосл букву в след назв города в списке и выводит find - находить, corresponds- соответствует
# если даже один город из списка не соотв получаем -нет ,blocked - блокированные
#

listCities = input('Введите список городов: \n ').lower().split()
blocked = ['ь', 'ъ', 'ы'] #эти буквы не считаются

corresponds = True
# result = 'da'  # var 2

for i in range(len(listCities) - 1):

    if listCities[i][-1] in blocked:  # если встретяться буквы из blocked переходим в след буквы с конца
        letter = listCities[i][-2]
    else:
        letter = listCities[i][-1]

    if listCities[i + 1][0] != letter:
        corresponds = False

#   var 2
result = 'net'
if corresponds:
    print('Есть')
else:
    print('Нет')

print(result)

# var2

# for & while primery
import time

# var. 1
temp = int(input('Ведите температуру: '))
if temp <= 50:
    print('Продолжаем работать')
    time.sleep(1)
    # temp = int(input('Введите температуру: '))

else:
    print('Работа останавливается')


# var.2

temp = int(input('Ведите температуру: '))

while temp <= 50:
    print('Работа продолжается')
    time.sleep(1)
    temp = int(input('Ведите температуру: '))

print('Остановить работу!')


# Primer 3

while True:
    print('Пока истина(while true) бесконечный цикл.')
    time.sleep(1)

# Primer 4 выбирать -choose

print('Вы в замке, есть дверь направо, налево, вперёд')

choose = input("Выберите: направо, налево, вперёд: ")

while choose != 'направо' and choose != 'налево' and choose != 'вперёд':
    print("Не правильный выбор, нет такого варианта!")
    choose = input("Выберите: направо, налево, вперёд: ")

if choose == 'направо':
    print("Вы видите большую комнату, там спуск в подвал")
    choose = input('Выберите: вернуться назад, спуститься: ')
    if choose == 'вернуться':
        print('А там уже дракон')
        print('Он вас съел')
        print("Игра закончился! Game over! ")
        # если выбрал спуститься
    else:
        print('Вы видите корону')
        choose = input(' Выберите: надеть или не надевать: ')

        while choose != 'надеть' and choose != 'надевать':
            print("Не правильный выбор, нет такого варианта!")
            choose = input(' Выберите: надеть или не надевать: ')

        if choose == 'надеть':
            print('В подвал врывается дракон, но вы уже надели корону и вы Повелитель дракона ')
            print('Вам с драконом предстоит много замечательных приключений')
            print('С победой!')

        else:
            print('В подвал вырывается дракон и съедает вас')
            print("Игра закончился! Game over!")

elif choose == 'налево':
    print('Вас встретил дракон и съел')
    print("Игра закончился! Game over!")

# тогда вперёд
else:
    print('Вы вышли из замка, вам все равно не спастись от дракона')
    print("Игра закончился! Game over!")


# PRIMER 5

login = input('Введите логин: ')
password = input('Введите пароль')

while login != 'admin' or password != ' 123456':

    print("Логин и пароль неверны !")
    login = input('Введите логин: ')
    password = input('Введите пароль')

print('Успешный вход')

#  PRIMER 6

login = input('Введите логин: ')
password = input('Введите пароль: ')

while login != 'admin' or password != '123':
    if login != 'admin':
        if password != '123':
            print("Логин и пароль неверный")
        else:
            print('Логин неверный')
    else:
        print('Пароль неверный')

    login = input('Введите логин: ')
    password = input('Введите пароль: ')

print('Успешный вход!')

    # PRIMER 7

command = input('Введите команду: ')

while command != 'выход':
    if command == '+':
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите первое число: '))
        print('Summa', num1 + num2)

    elif command == '-':
        num1 = float(input('Введите уменьшаемое: '))
        num2 = float(input('Введите вычитаемое: '))
        print('Разность', num1 - num2 )

    elif command == '*':
        num1 = float(input('Введите 1-го множителя: '))
        num2 = float(input('Введите 2-го множителя: '))
        print('Произведение', num1 * num2)

    elif command == '/':
        num1 = float(input('Введите делимое: '))
        num2 = float(input('Введите делителя: '))
        print('Частное', '%.2f' %(num1 / num2))

    else:
        print('Неизвестная команда')

    command = input('Введите команду: ')

print("Калькулятор закрыт")

# PRINER.8_ ALISA
#
print('Алиса может прочитать вам сказку,стихи или рассказать анекдот.')
command = input('Выберите: сказка, стихи, анекдот, мудрый совет или выход: ')

while command != 'выход':
    if command == 'сказка':
        print('Жили-были дед и бабка. Жили они долго и счастливо!')
        question = input('Как вам сказка?,выберите - хорошо или отлично: ')

        while question != 'exit':
            if question == 'отлично' or question == 'хорошо':
                print('Алиса большой молодец!')
                break
            elif question == 'так себе' or question == 'нормально':
                skazka = input(' Может другую сказку?: ')
                if skazka == 'da':
                    print('Жили-были дед,бабка, внучка и их корова. Жили они долго,сыто и счастливо!')
                    question = input('Как вам это сказка?: ')
                    if question == 'отлично' or question == 'хорошо':
                        print('Всё таки Алиса большой молодец!')

                    else:
                        print('Хмм, жаль')
                else:
                    print('Тогда пока!')
                    break
            else:
                print('Такой оценки нет, у нас либо отлично,либо хорошо!')
                print('Другого не предусмотрено.')
                question = input('Выберите хорошо или отлично: ')


        print('Заглядывайте по чаще!')
        break

    elif command == 'анекдот':
        print('Давай мне больше денег, я хочу большей финансовой независимости.')
        question = input('Ахахахахах, смешно?:')
        if question == 'да':
            print('У нас всегда весело.')
            print('Заглядывайте по чаще!')
            break
        else:
            print('Ладушки,в другой раз!')
            break
    elif command == 'мудрый совет':
        print('Если правда против вас, повернитесь к ней спиной, и она будет за вами! ')

print('Алиса не прошается с вами,до новых встреч!')





# PRIMER.8
step = 1
while step < 6:
    print('Шаг 1.')
    print('Шаг 2.')
    print('Шаг 3.')
    print('Шаг 4.')
    print('Шаг 5.')
    step = step + 1
step = 10
while 0 < step <= 10:
    print(step - 1)
    step = step -1
    if step == 0:
        print('bumm!')





# Программа выводит по выбранной команде итог, choice - vybor
help = '*', '/', "+", '-'
command = input('Пожалуйста введите команду: ')

if command == 'help':
    print('help')
elif command == '*':
    num1 = float(input('Введите 1-го множителя: '))
    num2 = float(input('Введите 2-го множителя: '))
    result = (num1 * num2)
    print( num1,'*', num2, '=', result)

elif command == '/':
    num1 = float(input('Введите делимое: '))
    num2 = float(input('Введите делитель: '))
    result = (num1 / num2)
    print(num1, '/', num2, '=', result)

elif command == '+':
    num1 = float(input('Введите 1-е слагаемое: '))
    num2 = float(input('Введите 2-е слагаемое'))
    result = (num1 + num2)
    print('Сумма', num1, '+', num2, '=', result)


elif command == '-':
    num1 = float(input('Введите уменьшаемое: '))
    num2 = float(input('Введите вычитаемое: '))
    result = (num1 - num2)
    print('Разность', num1, '-', num2, '=', result)

else:
    print('Упсс, что-то нито,исправтье ошибку!')

# Номер, месяц = период года

monthNumber = int(input('Введите номер месяца: '))
if monthNumber == 12 or monthNumber == 1 or monthNumber == 2:
    print('Вы ввели цифру', str(monthNumber) + ', это зима.')
elif monthNumber == 9 or monthNumber == 10 or monthNumber == 11:
    print('Вы ввели цифру', str(monthNumber) + ',это осень.')

elif monthNumber == 6 or monthNumber == 7 or monthNumber == 8:
    print('Вы ввели цифру', str(monthNumber) + ',это лето.')

elif monthNumber == 3or monthNumber == 4 or monthNumber == 5:
    print('Вы ввели цифру', str(monthNumber) + ', это весна.')

else:
    print('Упсс, вы ввели неправильную цифру. ')

# Вложенное ветвление

command = input('Введите команду: ')
if command == 'сказка':
    print('Жили-были бабушка и дедушка')
    print('Спокойной ночи!')
else:
    if command == 'а        некдот':
        print('Подскользнулся упал, очнулся гипс')
    else:
        if command == 'сoвет':
            print('Здоровья надо беречь смолоду')
        else:
            if command == 'афоризм':
                print('bdi')
            else:
                print('ne ponyatno chto hotite')
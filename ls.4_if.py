'''
Вевтвления- if, else, elif. Primery
'''

login = input('Введите логин: ')
passw = input('Введите пароль: ')
if login == 'test' and passw == '123':
    print('Hi, Inga!')
    print('Вы успешно авторизовались!')
else:
    print('Пароль млм логин не верный')
    print('Попробуйте еще раз')

# Zadacha 1

word = input('Что вы желаете на обед?: ')
if word == 'краба':
    print('Интересный у вас вкус, краб-отличный выбор!')
if word != 'краба':
    print('Хорошо,аказ принята')

# Zadacha 2
weather = int(input('Какая сегодня погода?: '))

if weather >= 25:
    print('Слишком жарко!')
    print('Включаю кондиционер')
if weather > 14 < 25:
    print('Хорошая погода!')
else:
    print('Прохладно!')

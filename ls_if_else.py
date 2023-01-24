LOG = 'test'  # LOG и PASSW -константы. Константа — это постоянная переменная,
PASSW = '123'  # значение которой нельзя изменить.

# Zadacha.1
log = input('Ведите свой логин: ')
passw = input('Введите пароль: ')

if log == LOG and passw == PASSW:
    print('Ура,вы удачно авторизовались!')
elif log == LOG and passw != PASSW:
    print('Не правильно введен пароль!')
    print('Попробуйте еще раз')
elif log != LOG and passw == PASSW:
    print('Не правильно введен логин')
    print('Попробуйте еще раз!')

elif log != LOG and passw != PASSW:
    print('Логин и пароль введен неверно!')
    print('Попробуйте еще раз или восстановите логин и пароль')

# Zadaxa. 2
# air_temp - темп воздуха, air_humid-влажность

air_temp = int(input('Введите температуру: '))
air_humid = int(input('Введите влажность: '))

if air_humid > 60 and air_temp < 10 or air_humid < 30 and air_temp > 30:
    print('Тревога!')

if not air_humid > 60 and air_temp < 10 or air_humid < 30 and air_temp > 30:
    print('Everything Ok!')

# # varian 2
air_temp = int(input('Введите температуру: '))
air_humid = int(input('Введите влажность: '))

danger = air_humid > 60 and air_temp > 30 or air_humid < 30 and air_temp > 30
if danger == danger:
    print('Тревога!')

else:
    print('Everything Ok!')

# Zadaxa.3
# срок служба колеса авто,если срок более 5 лет,заменить: wheel -колеса

# 1

wheel_1 = int(input('Выедите срок службы 1-го колеса: '))
wheel_2 = int(input('Выедите срок службы 2-го колеса: '))
wheel_3 = int(input('Выедите срок службы 3-го колеса: '))
wheel_4 = int(input('Выедите срок службы 4-го колеса: '))

is_suitable = wheel_1 <= 6 and wheel_2 <= 6 and wheel_3 <= 6 and wheel_4 <= 6
if wheel_1 >= 6:
    print('Пора заменить 1-e колесо!')
if wheel_2 >= 6:
    print('Пора заменить 2-e колесо!')
if wheel_3 >= 6:
    print('Пора заменить 3-e колесо!')
if wheel_4 >= 6:
    print('Пора заменить 4-e колесо!')
else:
    print('Все отлично,счастливой дороги!')

# 2
if is_suitable:
    print('Все отлично,счастливой дороги!')
if not is_suitable:
    print('Замените колесо которому 6 и более лет!')

# Zadacha 3
client_1 = float(input('Какую сумму клиент потратил за квартал ?: '))

todays_expenses_1 = float(input('Общая сумма сегодня покупки составляет: '))

per_quarter_1 = 6000
todays_expenses = 5000

if client_1 >= per_quarter_1:
    print('Оо, у вас хорошие бонусы')
    print('Вам полагается скидка 12% от сегодняшней покупки')
    print('Пожалуйста с учетом скидок: ', todays_expenses_1 - (todays_expenses_1 * 0.12), 'руб')

if todays_expenses_1 >= todays_expenses and client_1 <= per_quarter_1:
    print('Вам полагается скидка 6% от сегодняшней покупки')
    print('Пожалуйста с учетом скидок: ', todays_expenses_1 - (todays_expenses_1 * 0.06), 'руб')

if client_1 < per_quarter_1 and client_1 < todays_expenses:
    print('Пожалуйста с вас:', todays_expenses_1, 'руб')

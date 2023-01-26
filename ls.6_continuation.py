'''
Программа просить логин и пароль, при успешном вводе
пишет-успешный вход, добро пожаловать!
Если неверно-логин и пароль неверен.
Спасибо,что пользуетесь технологиями ХХ1 ВЕК Corporation!
'''
login = 'test'
passw = 'passw'
log = input('Пожалуйста введите логин: ')
pas = input('Пожалуйста введите пароль: ')
if log == login and pas == passw:
    print('Успешный вход!')
    print('Добро пожаловать!')
else:
    print('Логин или пароль неверный')

print("Спасибо, что пользуетесь технологиями 'XXI Corporation'")

'''
Проверка веса багажа, если больше 20 кг пишет больше 
нормы,если нет не перевышает нормы,
Самолет вылетает через 2 часа
'''
limit_bag = 20

passenger = float(input('Пожалуйсте введите вес багажа: '))
if passenger <= limit_bag:
    print('Всё в норме.')
    print('Проходите дальше и счастливого вам полета!')
else:
    print('Ваш багаж превышает норму на: ', "%.2f" % (passenger - limit_bag), 'kg')

"""
Программа запрашивает данные 3-х датчиков и если одно из них выше 0я
должно вывести две строчки- Опасность! Таяние льдов!(maximum_allowable - максимально допустимый)
"""
maximum_allowable = 0

sensor_1 = float(input('Введите данные 1-го датчика: '))
sensor_2 = float(input('Введите данные 2-го датчика: '))
sensor_3 = float(input('Введите данные 3-го датчика: '))

sensors = sensor_2, sensor_2, sensor_3
sos = sensor_1, sensor_2, sensor_3 > maximum_allowable

if sensor_1 > maximum_allowable:
    print('Датчик №1 превышает норму')
    print('Опасность!')
    print('Таяние льда!')
if sensor_2 > maximum_allowable:
    print('Датчик №2 превышает норму')
    print('Опасность!')
    print('Таяние льда!')

if sensor_3 > maximum_allowable:
    print('Датчик №3 превышает норму')
    print('Опасность!')
    print('Таяние льда!')

else:

    print('Данные датчиков не превышает норму!')

"""
Программа получает сумму мат помощи нуждющим. Если она больше 10000,нужно вычесть 
налог 1000 ри вывести итоговую сумму.
Если число меньше нужно добавить доп 500 р от спец фонда и вывести итог сумму,
если превыш и тут надо вычесть налог.
"""

person_1 = float(input('Ведите сумму финансовой помощи: '))
person_2 = float(input('Ведите сумму финансовой помощи: '))
person_3 = float(input('Ведите сумму финансовой помощи: '))
person_4 = float(input('Ведите сумму финансовой помощи: '))

min_sum = 10000

if person_1 >= min_sum:
    nalog = person_1 - (person_1 * 0.10)
    print('person_1, вам с учетом налогов к выплате: ', nalog, 'руб')

if person_2 >= min_sum:
    nalog = person_2 - (person_2 * 0.10)
    print('person_2, с учетом налогов к выплате: ', nalog, 'руб')

if person_3 >= min_sum:
    nalog = person_3 - (person_3 * 0.10)
    print('person_3, с учетом налогов к выплате: ', nalog, 'руб')

if person_4 >= min_sum:
    nalog = person_4 - (person_4 * 0.10)
    print('person_4, с учетом налогов к выплате: ', nalog, 'руб')

if person_1 < min_sum:
    sum = float(person_1 + (min_sum - person_1))
    to_be_paid = (sum - (sum * 0.10))
    print('person_1, с учетом налогов к выплате: ', to_be_paid, 'руб')

if person_2 < min_sum:
    sum = float(person_2 + (min_sum - person_2))
    to_be_paid = (sum - (sum * 0.10))
    print('person_1, с учетом налогов к выплате: ', to_be_paid, 'руб')

if person_3 < min_sum:
    sum = float(person_3 + (min_sum - person_3))
    to_be_paid = (sum - (sum * 0.10))
    print('person_1, с учетом налогов к выплате: ', to_be_paid, 'руб')

if person_4 < min_sum:
    sum = float(person_4 + (min_sum - person_4))
    to_be_paid = (sum - (sum * 0.10))
    print('person_1, с учетом налогов к выплате: ', to_be_paid, 'руб')

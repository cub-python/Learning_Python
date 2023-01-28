# Программа спрашивает логин и пароль у юзера, если не правильно вывести Не правильно введен пароль  илогин,
# Если правильно вывести Добро пожаловать!
login = 'test'
password = '123'

login = input('Введите логин : ')
password = input('Введите логин : ')

if login == 'test' and password == '123':
    print('Успешно авторизовались')
    print('Добро пожаловать!')

elif login != 'test' and password != '123':
    print('Логин или пароль неверный')
    print('Попробуйте еще раз')

print('Спасибо,что пользуетесь технологиями Dad Corporation!')

'''
Аэропорт,стойка регистрации багажа. Если багаж более 15 кг,напишет багаж больше лимита
и на сколько кг больше и чере сколько вылетает самолет.
'''
limBag = 15
bag = float(input('Введите вес багажа: '))

if bag > 15:
    difference = float(bag - limBag)
    print('Ваш багаж больше нормы на', '%.2f' % difference, 'кг')
elif bag <= limBag:
    print('Ваш багаж в норме')
    print('Проходите,счастливого полета!')
else:
    print("Самолет вылетает через 2 часа")

'''
Тестирование крови на витамин D и йода. Программа запрашивает ФИО и 2 
числа сколько в крови йода и D витамина и отвечает в норме или превышает показатели.
'''
iodineNormMin = 15
iodineNormMax = 20
vitDmin = 30
vitDmax = 100

fullName = input('Введите ваше ФИО данные пожалуйста: ')
iodineContent = float(input('Сколько в крови пациента ioda: '))
vitDcontent = float(input('Сколько в крови пациента витамина D: '))

if iodineContent < iodineNormMin and vitDcontent < vitDmin:
    print('Уважаемый(ая) ', fullName,'ваши показатели йода ниже нормы на:','%.2f' %(iodineNormMin - iodineContent),'мг')
    print('а показатели витамина D нижде на: ','%.2f' %(vitDmin - vitDcontent),'нг')

elif iodineContent > iodineNormMax and vitDcontent > vitDmax:
    print('Уважаемый(ая)',fullName,'ваши показатели йода выше нормы на:', '%.2f' %(iodineContent - iodineNormMax),'мг')
    print('Уважаемый(ая)',fullName,'ваши показатели витамина выше нормы на:', '%.2f' %(vitDcontent - vitDmax),'мг')

else:
    print('Уважаемый(ая)', fullName, 'ваши показатели в норме')


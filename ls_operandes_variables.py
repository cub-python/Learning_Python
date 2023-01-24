# a - переменная
#  = - operator prisvaivania
# print - funktsia

a = 7
print(a)

#  peremennaia poluchaet 6.3
a = 7
a = 6.3

print(a)
# каскадное присваивание(1 объект присваивается к разным переменным)
a = b = c = 0
print(a, b, c)

# vyvodit - 0 0 0

# идентификатор id определ с помощью функции id

print(id(a), id(b), id(c))
# 139935294243024 139935294243024 139935294243024

a, b = 1, 2
print(a, b)
print(id(a), id(b))
# 1 2
# 140403775242480 140403775242512
# меняем значения
a, b = b, a
print(a, b)
# 2 1  динамическая типпизация
print(type(a))
# <class 'int'>


name = input('Как вас зовут ? - ')
name2 = input("А вас как зовут ? -")
print("Приятно познакомиться,", name, 'и', name2, "!")

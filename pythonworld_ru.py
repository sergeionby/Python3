#https://pythonworld.ru/osnovy/tasks.html

print('''
Task #1:
Написать функцию arithmetic, принимающую 3 аргумента:
первые 2 - числа, третий - операция, которая должна быть
произведена над ними. Если третий аргумент +, сложить их;
если —, то вычесть; * — умножить; / — разделить(первое
на второе). В остальных случаях вернуть строку
"Неизвестная операция".''')

def arithmetic(x,y,z):
    if z == '+' : return (x + y)
    elif z == '-' : return (x - y)
    elif z == '*' : return (x * y)
    elif z == '/' : return (x / y)
    else: return 'Unknown operation'

a = 4
b = 5
c = ('+', '-', '*', '/', '?', '')

for i in c:
    print(a, i, b, '-->', arithmetic(a,b,i))


print('''\n
Task #2:
Написать функцию is_year_leap, принимающую 1 аргумент — год,
и возвращающую True, если год високосный, и False иначе.''')

def is_year_leap(y):
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 ==0):
        return True
    else:
        return False

n = 400
print ('Высокосный ли год', n, '-->', is_year_leap(n))


print('''
Task #3
Написать функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
площадь квадрата и диагональ квадрата.''')

import math

def square(x):
    a = (x*4, x**2, round(math.sqrt(x*x + x*x),2))
    return a

print(square(5))


print('''
Task #4
Написать функцию season, принимающую 1 аргумент — номер
месяца (от 1 до 12), и возвращающую время года, которому
этот месяц принадлежит (зима, весна, лето или осень).''')

def season(m):
    if m in (12, 1, 2): return 'зима'
    elif m in (3, 4, 5): return 'весна'
    elif m in (6, 7, 8): return 'лето'
    elif m in (9, 10, 11): return 'осень'
    else: return 'Такого номера месяца не существует'

print(season(22))


print('''Пользователь делает вклад в размере a рублей сроком
на years лет под 10% годовых (каждый год размер его вклада
увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
и на них в следующем году тоже будут проценты).
Написать функцию bank, принимающая аргументы a и years, и
возвращающую сумму, которая будет на счету пользователя.''')

def bank(x, y, p = 0.1):
    if (y != 0) :
        x+=x*p
        y-=1
        return bank(x,y)
    else: return round(x, 2)

a = 100
years = 10

print(bank(a, years))


print('''
Task #6
Написать функцию is_prime, принимающую 1 аргумент — число
от 0 до 1000, и возвращающую True, если оно простое, и
False - иначе.''')

def is_prime(x):
    if x in (0, 1, 2): return False
    else:
        delitel = 0
        i = 2
        while (i <= x) and (delitel < 2):
            if (x %  i == 0):
                delitel += 1
                i+=1
            else: i += 1
        if (delitel == 1): return True
        else: return False

for i in range(10):
    print(i, '-->',  is_prime(i))


print('''
Task #7
Написать функцию date, принимающую 3 аргумента — день,
месяц и год. Вернуть True, если такая дата есть в нашем
календаре, и False иначе.''')

import datetime

def date(d, m, y):
    try:
        datetime.date(y, m, d)
    except ValueError:
        return False
    else:
        return True

print(date(30, 6, 2021))
print(date(31, 6, 2021))
print(date(31, 2, 2021))

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

# -*- coding: utf-8 -*-

# Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами. 
# Если это возможно, выведите строку YES, иначе выведите строку NO.
# Треугольник — это три точки, не лежащие на одной прямой.


def is_triangle(x=(input('Введите три значения длинн сторон: '))):
    lengths = x.split(' ')
    a = int(lengths[0])
    b = int(lengths[1])
    c = int(lengths[2])
    
    if a + b > c and a + c > b and b + c > a:
        return 'Да, с такими значениями можно построить треугольник!'
    else:
        return 'Нет, данные значения не подходят для построения треугольника!'


print(is_triangle())

from math import *   # Подключение модуля math
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))
if x + pow(fabs(y), 1./4) > 0:
    a1 = 5*atan(x)
    a2 = 1/4*acos(x)
    a3 = fabs(x-y)+(x**2)/fabs(x-y)*z
    a4 = a2*a3
    s = a1-a4
    print("Результат ", s)
else:
    print("Значение выражения не может быть вычислено")

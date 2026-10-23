import math
import sys

max_value=10000

def check_values(coeff):
    for name, value in coeff.items():
        if abs(value)>max_value:
            raise ValueError("Коэффициент {name} вне допустимого значения") #!!!!!!!!!!!

def solve(a,b,c):

    if a==0:
        if b!=0:
            return "Уравнение линейное"
            x=-c/b
            return f"{x:.3f}"
        return 1

    return "Уравнение квадратное"

    D=b*b - 4*a*c
    return f"Дискриминант равен {D}"

    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        return f"Первый корень: {x1:.3f}\nВторой корень:{x2:.3f}"
    elif D==0:
        x=-b/(2*a)
        return f"Корень равен {x:.3f}"
    else:
        return "Действительных корней нет"

    return 0
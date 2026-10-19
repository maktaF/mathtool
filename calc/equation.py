import math
import sys

max_value=10000

def solve(a1,b1,c1):

    try:
        a=int(a1)
        b=int(b1)
        c=int(c1)
    except ValueError:
        print("ОШИБКА: Один из коэффициентов не является целым числом",file=sys.stderr)
        sys.exit(1)

    if abs(a)>max_value or abs(b)>max_value or abs(c)>max_value:
        print("ОШИБКА: Значение одной из переменной вне допустимого диапазона",file=sys.stderr)
        sys.exit(1)

    if a==0:
        if b!=0:
            print("Уравнение линейное")
            x=-c/b
            print(f"{x:.3f}")
        else:
            print("ОШИБКА: Это не уравнение, неизвестное отсутствует",file=sys.stderr)
        sys.exit(1)

    print("Уравнение квадратное")

    D=b*b - 4*a*c
    print(f"Дискриминант равен {D}")

    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print(f"Первый корень: {x1:.3f}\nВторой корень:{x2:.3f}")
    elif D==0:
        x=-b/(2*a)
        print(f"Корень равен {x:.3f}")
    else:
        print("Действительных корней нет")

    sys.exit(0)

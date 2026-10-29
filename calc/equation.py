import math

max_value=10000

def check_values(coeff):
    for name, value in coeff.items():
        if abs(value)>max_value:
            raise ValueError(f"Коэффициент {name} вне допустимого значения")
    if coeff["A"]==0 and coeff["B"]==0:
        raise ValueError("Это не уравнение")

def solve(a,b,c):

    if a==0:
        return "Lинейное",None, [-c/b]

    D=b*b - 4*a*c

    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        return "Квадратное", D, [x1,x2]
    elif D==0:
        return "Квадратное", D, [-b/(2*a)]
    return "Квадратное",D,[]
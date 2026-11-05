import math

MAX_ITERATE=100000

def ratio(x):
    return x/(x+1)

def root(x):
    return math.sqrt(x*x+1)

FUNCTIONS = {
    "ratio": (ratio, "F(x) = x/(x+1)", 0, 20, True),
    "root": (root, "F(x) = sqrt(x^2 + 1)", -5, 5, False)
}

def check_prm(a,b,steps,low,high,f):
    '''Проверка значений на ограничения, количество шагов'''
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("ОШИБКА: Предел интегрирования не является конечным числом")
    if a>=b:
        raise ValueError("ОШИБКА: Начальный предел не меньше конечного")
    if f:
        p = low<=a<=high and low<=b<=high
    else:
        p = low<a<high and low <b<high
    if not p:
        raise ValueError("ОШИБКА: Предел вне промежутка")
    if not 1<=steps<=MAX_ITERATE:
        raise ValueError("ОШИБКА: Количество шагов вне диапазона")


def integrate(f,a,b,steps):
    '''Приближенное вычисление интегралов'''
    dx = (b-a)/steps
    result=0
    for i in range(0,steps):
        x=a+i*dx
        result+=f(x)*dx
    return result
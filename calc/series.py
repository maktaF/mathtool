import math

MAX_TERMS=10000
MAX_EPS=0.0001
MAX_ITERATIONS=100000
DIGITS=math.ceil(-math.log10(MAX_EPS))

def sing(n):
    '''Возврат знака с учетом номера'''
    if n%2==0:
        return -1
    else:
        return 1

def sqplus(n):
    '''Возврат n-й значение последовательнотси sqplus'''
    return sing(n)/(n*n+1)

def third(n):
    '''Возврат n-й значение последовательнотси third'''
    return sing(n)/(3*n)

FORMULAS={
    "sqplus": (sqplus, "S=1/(1^2+1) - 1/(2^2+1) + ..."),
    "third": (third, "S=1/3 - 1/6 + 1/9 - ...")
}

def check_terms(terms):
    '''Проверка значений на ограничения по количеству'''
    if not(1<=terms<=MAX_TERMS):
        raise ValueError("ОШИБКА: Количество слагаемых вне диапазона")

def check_eps(eps):
    '''Проверка значений на ограничения по точности'''
    if not(math.isfinite(eps)) or not(0<eps<=MAX_EPS):
        raise ValueError("ОШИБКА: Точность вне диапазона")

def sum_by_count(term,count):
    '''Вычисление суммы последовательности по количеству'''
    result = 0
    for n in range(1,count+1):
        result+=term(n)
    return result

def sum_by_eps(term,eps):
    '''Вычисление суммы последовательности по точности'''
    result=0
    n=0
    for n in range(1,MAX_ITERATIONS+1):
        value=term(n)
        result+=value
        if abs(value)<eps:
            return result,n
        n+=1
    raise ValueError("ОШИБКА: Точность не достигнута")
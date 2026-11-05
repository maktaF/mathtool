import math

MAX_VALUE=20
MAX_ABS=10000

def check_num(numbers):
    '''Проверка содержания списка и кол-во значений в нем; проверка ограничений значений в списке'''
    if len(numbers)==0:
        raise ValueError("ОШИБКА: Список значений пуст")
    elif len(numbers)>MAX_VALUE:
        raise ValueError(f"ОШИБКА: Кол-во чисел больше {MAX_VALUE}-ти")
    for number in numbers:
        if not math.isfinite(number):
            raise ValueError("ОШИБКА: Значение не является конечным")
        elif abs(number)>MAX_ABS:
            raise ValueError("ОШИБКА: Значение по модулю больше 10000")                


def summ(numbers):
    '''Сумма списка'''
    result=0
    for i in numbers:
        result+=i
    return result

def sred(numbers):
    '''Среднее арифметическое списка'''
    return sum(numbers)/len(numbers)

def mini(numbers):
    '''Наименьшее значение в списке'''
    result=numbers[0]
    for i in numbers:
        if i<result:
            result=i
    return result

def len_good(numbers):
    '''Кол-во положительных чисел'''
    result=0
    for i in numbers:
        if i>0:
            result+=1
    return result

def len_bad(numbers):
    '''Кол-во отрицательных чисел'''
    result=0
    for i in numbers:
        if i<0:
            result+=1
    return result

def sum_kv_otkl(numbers):
    '''Сумма квадратов отклонений'''
    sr_znach=sred(numbers)
    result=0
    for i in numbers:
        result+=((i-sred(numbers))**2)
    return result

def disp(numbers):
    '''Дисперсия'''
    return sum_kv_otkl(numbers)/len(numbers)

def st_otkl(numbers):
    '''Стандартное отклонение'''
    if len(numbers)<2:
        return None
    return math.sqrt(sum_kv_otkl(numbers)/(len(numbers)-1))

def maxi(numbers):
    '''Наибольшее значение в списке'''
    result=numbers[0]
    for i in numbers:
        if i>result:
            result=i
    return result

def sum_kv(numbers):
    '''Сумма квадратов значений в списке'''
    result=0
    for i in numbers:
        result+=i**2
    return result

def sr_kv(numbers):
    '''Среднее квадратичное значений'''
    result=sum_kv(numbers)/len(numbers)
    return math.sqrt(result)

def sko(numbers):
    '''Сумма квадратов отклонений'''
    return math.sqrt(disp(numbers))


REPORT=[
    ("Количество",len,"d"),
    ("Сумма",summ,".3f"),
    ("Ср. арифм.",sred,".3f"),
    ("Наименьшее",mini,".3f"),
    ("Наибольшее",maxi,".3f"),
    ("Отрицательных",len_bad,"d"),
    ("Положительных",len_good,"d"),
    ("СКО",sko,".3f"),
    ("Дисперсия",disp,".3f"),
    ("Станд.отклонение",st_otkl,".3f"),
    ("Сумма кв.",sum_kv,".3f"),
    ("Среднее кв-ое",sr_kv,".3f"),
]
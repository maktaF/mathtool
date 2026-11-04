import math

MAX_VALUE=20
MAX_ABS=10000

def check_num(numbers):
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
    result=0
    for i in numbers:
        result+=i
    return result

def sred(numbers):
    return sum(numbers)/len(numbers)

def mini(numbers):
    result=numbers[0]
    for i in numbers:
        if i<result:
            result=i
    return result

def len_good(numbers):
    result=0
    for i in numbers:
        if i>0:
            result+=1
    return result

def len_bad(numbers):
    result=0
    for i in numbers:
        if i<0:
            result+=1
    return result

def sum_kv_otkl(numbers):
    sr_znach=sred(numbers)
    result=0
    for i in numbers:
        result+=((i-sred(numbers))**2)
    return result

def disp(numbers):
    return sum_kv_otkl(numbers)/len(numbers)

def st_otkl(numbers):
    if len(numbers)<2:
        return None
    return math.sqrt(sum_kv_otkl(numbers)/(len(numbers)-1))

def maxi(numbers):
    result=numbers[0]
    for i in numbers:
        if i>result:
            result=i
    return result

def sum_kv(numbers):
    result=0
    for i in numbers:
        result+=i**2
    return result

def sr_kv(numbers):
    result=sum_kv(numbers)/len(numbers)
    return math.sqrt(result)

def sko(numbers):
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
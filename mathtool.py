
import sys
import math

def print_help():
    print(
        "Mathtool - решение уранений вида a*x^2 + b*x + c = 0\n" \
        "Инструкция:\n" \
        "python mathtool.py  ->  вывод справки\n" \
        "python mathtool.py --help  ->  вывод справки\n" \
        "python mathtool.py solve  ->  ввод коэффициентов с клавиатуры\n" \
        "python nathtool.py solve -a 1 -b -3 -c 2  ->  решение с заданным коэфициентами\n" \
        "Примечание: a,b,c - целые числа, не превышающие 10000 по модулю."
    )

def main():
    if len(sys.argv)==1 or sys.argv[1]=="--help":
        print_help()
        sys.exit(0)
    elif sys.argv[1]!="solve":
        print("ОШИБКА: Неизестная команда",file=sys.stderr)
        sys.exit(1)
    elif len(sys.argv)==2 and sys.argv[1]=="solve":
        a1=int(input("Введите параметр -a: "))
        b1=int(input("Введите параметр -b: "))
        c1=int(input("Введите параметр -c: "))
    elif len(sys.argv)==8:
        if sys.argv[2]!="-a" or sys.argv[4]!="-b" or sys.argv[6]!="-c":
            print("ОШИБКА: Неизвестный параметр",file=sys.stderr)
            sys.exit(1)
        else:
            a1=sys.argv[3]
            b1=sys.argv[5]
            c1=sys.argv[7]
    else:
        print("ОШИБКА: Неправильный набор параметров",file=sys.stderr)
        sys.exit(1)


    try:
        a=int(a1)
        b=int(b1)
        c=int(c1)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом",file=sys.stderr)
        sys.exit(1)


    if abs(a)>10000 or abs(b)>10000 or abs(c)>10000:
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
    
main()
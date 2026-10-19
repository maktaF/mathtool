
import sys
import math
from calc import equation

def print_help():
    print(
        "Mathtool - решение уранений вида a*x^2 + b*x + c = 0\n" \
        "Инструкция:\n" \
        "python mathtool.py  ->  вывод справки\n" \
        "python mathtool.py --help  ->  вывод справки\n" \
        "python mathtool.py <komanda> --help  ->  справка по команде\n"\
        "\n"\
        "python mathtool.py solve  ->  ввод коэффициентов с клавиатуры\n" \
        "python nathtool.py solve -a 1 -b -3 -c 2  ->  решение с заданным коэфициентами\n" \
        "Примечание: a,b,c - целые числа, не превышающие 10000 по модулю.\n"\
        "\n"\
        "python mathtool.py stats --input number.txt  -> показатели последовательности\n"\
        "python mathtool.py series --func sqplus --terms 6\n"\
        "python mathtool.py series --func sqplus --eps 0.0001\n"\
        "python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000\n"\
    )

def main():
    if len(sys.argv)==1 or sys.argv[1]=="--help":
        print_help()
        sys.exit(0)
    elif sys.argv[1]!="solve":
        print("ОШИБКА: Неизестная команда",file=sys.stderr)
        sys.exit(1)
    elif len(sys.argv)==2 and sys.argv[1]=="solve":
        a1=input("Введите параметр -a: ")
        b1=input("Введите параметр -b: ")
        c1=input("Введите параметр -c: ")
        equation.solve(a1,b1,c1)
    elif len(sys.argv)==8:
        if sys.argv[2]!="-a" or sys.argv[4]!="-b" or sys.argv[6]!="-c":
            print("ОШИБКА: Неизвестный параметр",file=sys.stderr)
            sys.exit(1)
        else:
            a1=sys.argv[3]
            b1=sys.argv[5]
            c1=sys.argv[7]
            equation.solve(a1,b1,c1)
    else:
        print("ОШИБКА: Неправильный набор параметров",file=sys.stderr)
        sys.exit(1)

main()
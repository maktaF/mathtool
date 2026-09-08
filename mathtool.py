
import sys

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
    if len(sys.argv)==0 or sys.argv[0]=="--help":
        print_help()
        sys.exit(0)
    if len(sys.argv)>=1 and sys.argv[1]!="solve":
        print("Неизестная команда",file=sys.stderr)
        sys.exit(1)
    if len(sys.argv)==1 and sys.argv[1]=="solve":
        a=int(input("Введите параметр -a:"))
        b=int(input("Введите параметр -b:"))
        c=int(input("Введите параметр -c:"))
    elif len(sys.argv)==7:
        if sys.argv[2]!="-a" or sys.argv[4]!="-b" or sys.argv[6]!="-c":
            print("Неизвестный параметр",file=sys.stderr)
            sys.exit(1)
    else:
        print("Неправильный набор параметров",file=sys.stderr)
if __name__=="__main__":
    main()
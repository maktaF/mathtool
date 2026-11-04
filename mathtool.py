import sys
import math
from cli import build_parser
from calc import equation,stats,series

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == None:
        parser.print_help()
    
    try:
        if args.command=="solve":
            return handle_solve(args)
        elif args.command=="stats":
            return handle_stats(args)
        elif args.command=="series":
            return handle_series(args)
    except (ValueError,OSError) as error:
        print(f"{error}", file=sys.stderr)

def handle_solve(args):
    values=(args.a,args.b,args.c)

    if all(value is None for value in values):
        try:
            a=int(input("Введите А: "))
            b=int(input("Введите B: "))
            c=int(input("Введите C: "))
        except ValueError:
            raise ValueError("Коэффициент не является целым числом")
    elif all(value is not None for value in values):
        a,b,c=values
    else:
        raise ValueError("Укажите все три аргумента либо ни одного")

    equation.check_values({"A": a, "B": b, "C": c})
    kind,d,roots=equation.solve(a,b,c)
    return f"{kind} уравнение\nДискриминант: {d}\nКорни: {roots}"

def handle_stats(args):
    numbers=[]
    if args.input is not None:
        try:
            with open(args.input, encoding="utf-8-sig") as file:
                for line in file:
                    for word in line.split():
                        try:
                            word=float(word)
                        except ValueError:
                            raise ValueError(f"ОШИБКА: \"{word}\" не является числом")
                        numbers.append(word)
        except OSError:
            raise OSError("Файл не открывается")
    else:
        for line in sys.stdin:
            for word in line.split():
                try:
                    word=float(word)
                except ValueError:
                    raise ValueError(f"ОШИБКА: \"{word}\" не является числом")
                numbers.append(word)

    stats.check_num(numbers)
    for label,function,form in stats.REPORT:
        value=function(numbers)
        if value is None:
            return f"{label} НЕ СУЩЕСТВУЕТ"
        else:
            print(f"{label}: {value:{form}}")

def handle_series(args):
    term,formula=series.FORMULAS[args.func]
    if args.terms is not None:
        series.check_terms(args.terms)
        count=args.terms
        result=series.sum_by_count(term,count)
    else:
        series.check_eps(args.eps)
        result,count=series.sum_by_eps(term,args.eps)
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
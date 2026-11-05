import sys
import math
from cli import build_parser
from calc import equation,stats,series,integration

def handle_solve(args):
    '''Чтение коэффициентов, решение уравнения и вывод его корней'''
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
    print(f"{kind} уравнение\nДискриминант: {d}\nКорни: {roots}")
    return 0

def handle_stats(args):
    '''Чтение чисел, выводит одиннадцать показателей'''
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
            print(f"{label} НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")

def handle_series(args):
    '''Вывод суммы ряда по количеству или точности'''
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

def handle_integration(args):
    '''Вывод значения интеграла, проверка пределов'''
    f,formula,low,high,i=integration.FUNCTIONS[args.func]
    integration.check_prm(args.start,args.to,args.steps,low,high,i)
    result=integration.integrate(f,args.start,args.to,args.steps)
    print(formula)
    print(f"Значение интеграла: {result:.4f}")
    return 0

COMM={
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integration
}

def main(argv):
    '''Запуск одной из команд и вывод его результата'''
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == None:
        parser.print_help()
    else:
        try:
            return COMM[args.command](args)
        except (ValueError,OSError) as error:
            print(f"{error}", file=sys.stderr)
            return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
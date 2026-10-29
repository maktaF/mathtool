import sys
from cli import build_parser
from calc import equation

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == None:
        parser.print_help()
        return 0
    
    try:
        if args.command=="solve":
            return handle_solve(args)
        return 0
    except (ValueError,OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

def handle_solve(args):
    values=(args.a,args.b,args.c)

    if all(value is None for value in values):
        try:
            a=int(input("Введите А: "))
            b=int(input("Введите B: "))
            c=int(input("Введите C: "))
        except ValueError:
            raise ValueError("Один из коэффициентов не является целым числом")
    elif all(value is not None for value in values):
        a,b,c=values
    else:
        raise ValueError("Укажите все три аргумента либо ни одного")

    equation.check_values({"A": a, "B": b, "C": c})
    kind,d,roots=equation.solve(a,b,c)
    return f"{kind} уравнение\nДискриминант: {d}\nКорни: {roots}"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
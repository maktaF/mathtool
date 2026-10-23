import sys
from cli import build_parser
from calc import equation

from . import cli

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

    if equation.check_values({"A": args.a, "B": args.b, "C": args.c}):
        equation.solve(args.a,args.b,args.c)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
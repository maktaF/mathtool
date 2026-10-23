import argparse
def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="Расчеты уравнения и числовых последовательностей",
        allow_abbrev=False
        )
    
    commands = parser.add_subparsers(dest="command")

    solve_parser = commands.add_parser(
        "solve",
        help="Решение уравнений",
        allow_abbrev=False
    )
    solve_parser.add_argument("-a",type=int)
    solve_parser.add_argument("-b",type=int)
    solve_parser.add_argument("-c",type=int)

    stats_parser = commands.add_parser(
        "stats",
        help="Показатели последовательности",
        allow_abbrev=False
    )
    stats_parser.add_argument("--input")

    series_parser = commands.add_parser(
        "series",
        help="Сумма ряда",
        allow_abbrev=False
    )
    series_parser.add_argument("--func", required=True)
    series_group = series_parser.add_mutually_exclusive_group(required=True)
    series_group.add_argument("--terms",type=int)
    series_group.add_argument("--eps",type=float)

    integrate_parser = commands.add_parser(
        "integrate",
        help="Численное интегрирование",
        allow_abbrev=False
    )
    integrate_parser.add_argument("--func",required=True)
    integrate_parser.add_argument("--from",dest="start",type=float,required=True)
    integrate_parser.add_argument("--to",type=float,required=True)
    integrate_parser.add_argument("--steps",type=int,required=True)

    return parser
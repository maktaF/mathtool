import argparse
from calc.series import FORMULAS
from calc.integration import FUNCTIONS

def build_parser():
    '''Создание разборщика и все четыре подкоманды'''
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
    solve_parser.add_argument("-a",help="Коэффициент A",type=int)
    solve_parser.add_argument("-b",help="Коэффициент В",type=int)
    solve_parser.add_argument("-c",help="Коэффициент С",type=int)

    stats_parser = commands.add_parser(
        "stats",
        help="Показатели последовательности",
        allow_abbrev=False
    )
    stats_parser.add_argument("--input",help="Файл со значениями")

    series_parser = commands.add_parser(
        "series",
        help="Сумма ряда",
        allow_abbrev=False
    )
    series_parser.add_argument("--func",help="Какой ряд суммировать", choices=sorted(FORMULAS), required=True)
    series_group = series_parser.add_mutually_exclusive_group(required=True)
    series_group.add_argument("--terms", help="Сколько слагаемых сложить [1,10000]",type=int)
    series_group.add_argument("--eps", help="До какой величины слагаемого считать (0,0.0001]",type=float)

    integrate_parser = commands.add_parser(
        "integrate",
        help="Численное интегрирование",
        allow_abbrev=False
    )
    integrate_parser.add_argument("--func", help="Какую функцию интегрировать", choices=sorted(FUNCTIONS),required=True)
    integrate_parser.add_argument("--from", help="Нижний предел интегрирования",dest="start",type=float,required=True)
    integrate_parser.add_argument("--to",help="Верхний предел интегрирования",type=float,required=True)
    integrate_parser.add_argument("--steps", help="На сколько прямоугольников делится отрезок [1,100000]",type=int,required=True)

    return parser
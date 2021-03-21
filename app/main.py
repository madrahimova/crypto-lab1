"""
Тестовое приложение
Исполнитель Мадрахимова Дарья <madrahim@cs.karelia.ru>, 2021
"""

from func.BigInt import rand

if __name__ == '__main__':
    p = rand(4)
    q = rand(4)

    p.print()
    q.print()
    p.sub(q).print()


"""
Генератор целых простых случайных больших чисел
Исполнитель Мадрахимова Дарья <madrahim@cs.karelia.ru>, 2021
"""

import random
from func.BigInt import BigInt


first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def __rand__(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def prime(n):
    while True:
        p = __rand__(n)
        for divisor in first_primes_list:
            if p % divisor == 0 and divisor ** 2 <= p:
                break
        else:
            return p


def passed(mrc):
    maxDivisionsByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert (2 ** maxDivisionsByTwo * ec == mrc - 1)

    def composite(tester):
        if pow(tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

    numberOfRTrials = 20
    for i in range(numberOfRTrials):
        tester = random.randrange(2, mrc)
        if composite(tester):
            return False
    return True


def rand():
    while True:
        p = prime(int(random.uniform(10, 1000)))
        if not passed(p):
            continue
        else:
            return BigInt(p)

"""
Библиотека длинной арифметики
Исполнитель Мадрахимова Дарья <madrahim@cs.karelia.ru>, 2021
"""

from __future__ import annotations
import numpy as np


class BigInt(object):
    def __init__(self, bigint: str):
        self.MAX = 10000
        self.bigint = bigint

        if np.char.isdigit(self.bigint[0]):
            self.bigint = self.bigint
            self.sign = False
        else:
            self.bigint = self.bigint[1:]
            self.sign = self.bigint[0] == '-'

    def __init__(self, bigint: int):
        self.MAX = 10000
        self.bigint = str(bigint)

        if np.char.isdigit(self.bigint[0]):
            self.bigint = self.bigint
            self.sign = False
        else:
            self.bigint = self.bigint[1:]
            self.sign = self.bigint[0] == '-'

    def str(self) -> str:
        return ('-' if self.sign else "") + self.bigint

    def pow(self, power) -> BigInt:
        if power > 1:
            return self.mul(self.pow(power - 1))
        else:
            return self

    def print(self):
        print(self.str())

    def equals(self, other: BigInt) -> bool:
        return self.bigint == other.bigint and self.sign == other.sign

    def less(self, other: BigInt) -> bool:
        if self.sign and not other.sign:
            return True
        elif not self.sign and other.sign:
            return False
        elif not self.sign:
            if len(self.bigint) < len(other.bigint):
                return True
            if len(self.bigint) > len(other.bigint):
                return False
            return self.bigint < other.bigint
        else:
            if len(self.bigint) > len(other.bigint):
                return True
            if len(self.bigint) < len(other.bigint):
                return False
            return self.bigint > other.bigint

    def greater(self, other: BigInt) -> bool:
        return not self.equals(other) and not self.less(other)

    def __init__(self, bigint: int):
        s = str(bigint)

        if np.char.isdigit(s[0]):
            self.bigint = s
            self.sign = False
        else:
            self.bigint = s[1:]
            self.sign = s[0] == '-'

    def abs(self) -> BigInt:
        return BigInt(self.bigint)

    def add(self, other: BigInt) -> BigInt:
        res = list(self.bigint if len(self.bigint) > len(other.bigint) else other.bigint)
        carry = '0'
        lenDiff = abs(len(self.bigint) - len(other.bigint))

        if len(self.bigint) > len(other.bigint):
            other.bigint = "".join(['0' for _ in range(lenDiff)]) + other.bigint
        else:
            self.bigint = "".join(['0' for _ in range(lenDiff)]) + self.bigint

        for i in reversed(range(len(res))):
            res[i] = str(int(carry) + int(self.bigint[i]) + int(other.bigint[i]))
            if i != 0:
                if int(res[i]) > 9:
                    res[i] = str(int(res[i]) - 10)
                    carry = '1'
                else:
                    carry = '0'

        if int(res[0]) > 9:
            res[0] = str(int(res[0]) - 10)
            res = '1' + "".join(res)

        res = "".join([str(e) for e in res])
        if self.sign == other.sign:
            res = ('-' if self.sign else "") + res
        else:
            if self.abs().greater(other.abs()):
                res = self.__sub__(other).str()
            else:
                res = other.__sub__(self).str()
        if res == '-0':
            return BigInt(res[1:])
        return BigInt(res)

    def sub(self, other: BigInt) -> BigInt:
        o = BigInt(other.bigint)
        o.sign = not other.sign
        return self.add(o)

    def __sub__(self, other: BigInt) -> BigInt:
        res = list(self.bigint if len(self.bigint) > len(other.bigint) else other.bigint)
        lenDiff = abs(len(self.bigint) - len(other.bigint))

        if len(self.bigint) > len(other.bigint):
            other.bigint = "".join(['0' for _ in range(lenDiff)]) + other.bigint
        else:
            self.bigint = "".join(['0' for _ in range(lenDiff)]) + self.bigint

        for i in reversed(range(len(res))):
            tmp = list(self.bigint)
            if tmp[i] < other.bigint[i]:
                tmp[i] = str(int(tmp[i]) + 10)
                tmp[i - 1] = str(int(tmp[i - 1]) - 1)
            self.bigint = tmp
            res[i] = str(int(self.bigint[i]) - int(other.bigint[i]))

        i = 0
        while res[i] == '0' and i < len(res) - 1:
            i += 1
        res = "".join([str(e) for e in res[i:]])
        return BigInt(res)

    def mul(self, other: BigInt) -> BigInt:
        if len(self.bigint) > len(other.bigint):
            tmp = self
            self = other
            other = tmp

        res = '0'
        r = BigInt(res)
        for i in reversed(range(len(self.bigint))):
            tmp = list(other.bigint)
            currDigit = int(self.bigint[i])
            carry = 0

            for j in reversed(range(len(tmp))):
                tmp[j] = int(tmp[j]) * currDigit + carry
                if tmp[j] > 9:
                    carry = int(tmp[j] // 10)
                    tmp[j] -= carry * 10
                else:
                    carry = 0

            if carry > 0:
                tmp = [carry] + tmp

            tmp += "".join(['0' for _ in range(len(self.bigint) - i - 1)])
            tmp = "".join([str(e) for e in tmp])
            r = BigInt(res).add(BigInt(tmp))

        r = r.bigint
        i = 0
        while r[i] == '0' and i < len(r) - 1:
            i += 1
        res = r[i:]
        return BigInt(('-' if self.sign != other.sign else "") + res)

    def divide(self, den: int) -> (BigInt, BigInt):
        rem = 0
        res = ""

        if den == 0:
            raise ZeroDivisionError()

        for i in range(len(self.bigint)):
            rem = rem * 10 + int(self.bigint[i])
            res += str(rem // abs(den))
            rem %= den
        res = ('-' if (den > 0 and self.sign) or (den < 0 and not self.sign) else "") + res[0:len(self.bigint)]
        return BigInt(res), BigInt(rem)

    def mod(self, other: BigInt) -> BigInt:
        den = int(other.bigint)
        _, rem = self.divide(den)
        rem.sign = self.sign != other.sign

        if rem.bigint == '0':
            rem.sign = False
        return rem

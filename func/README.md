# Алгоритмы
## BigInt - [библиотека длинной арифметики](https://github.com/meowbyte/crypto-lab1/blob/main/func/BigInt.py)
- BigInt(object) - создает большое число из строки или целого числа
  - bigint - строка большого числа
  - sign - знак большого числа
- print() - выводит большое число в консоль
```python
>>> BigInt(3).print()
3
```
- sub(other) - вычитает из одного большого числа другое
```python
>>> a = BigInt(5)
... b = BigInt(-10)
... a.sub(b).print()
15
```
- mul(other) - умножает одно большое число на другое
```python
>>> a.mul(b).print()
-50
```
- mod(other) - вычисляет остаток от деления одного большого числа на другое
```python
>>> a.mod(b).print()
-5
```
## Random - [генератор чисел для RSA](https://github.com/meowbyte/crypto-lab1/blob/main/func/Random.py)
- rand() - генерирует случайное целое простое большое число
```python
>>> rand().print()
2987101364995321223773889164037424951931205607551795741333751085747006493797150185334882823958926588591
```

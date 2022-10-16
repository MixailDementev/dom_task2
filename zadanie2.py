# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

num = int(input('input number: '))
f = 1
for i in range(num):
    i = i+1
    f = i*f
    print(f, end=' ')
print()


def f(x):
    return ((x == 1) and 1) or x * factorial(x - 1)

list2 = list(f(i) for i in range(1, num + 1))
print(list2)

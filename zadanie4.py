# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

from random import randint

N = int(input('-> '))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)

x = int(input('first position = '))
y = int(input('second position = '))

mult = numbers[x-1]*numbers[y-1]
print(f'Mult of elements: {numbers[x-1]} * {numbers[y-1]} =', mult)

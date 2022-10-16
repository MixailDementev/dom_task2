# Реализуйте алгоритм перемешивания списка.

from random import randint
import random

N = int(input('-> '))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print("Original List: ", numbers)

n = len(numbers)

for i in range(N):
    j = random.randint(0, N-1)
    element = numbers.pop(j)
    numbers.append(element)
print("Shuffled List: ", numbers)

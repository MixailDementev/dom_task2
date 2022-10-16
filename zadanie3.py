# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

num = int(input('input number: '))
n = 1
sum = 0
for i in range(1, num):
    i = i+1
    n = (1+1/n)**n
    sum = float(n)
    print(n, end=' ')
print()
print('the sum of the sequence numbers =', round(sum, 4))

# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
n = int(input('Введите размер массива N: '))
j = int(input('Введите максимальное число: '))
list = []
for i in range(n):
    list.append(randint(1, j))
x = int(input('Введите X: '))

min = 147483648
i_min = 0
for i in range(len(list)):
    temp = abs(list[i]-x)
    if temp < min:
        min = temp
        i_min = i
print(list)       
print(f' ближе всего к {x}: {list[i_min]}')
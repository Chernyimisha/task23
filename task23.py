# Задача №23. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

n = int(input('Введите количество элементов массива: '))
input_massive = []
count = 0

for i in range(n):
    input_massive.append(int(input('Введите значение элемента: ')))
    if input_massive[i] > input_massive[i-1]:
        count += 1

print(count)


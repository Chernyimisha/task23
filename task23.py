n = int(input('Введите количество элементов массива: '))
input_massive = []
count = 0

for i in range(n):
    input_massive.append(int(input('Введите значение элемента: ')))
    if input_massive[i] > input_massive[i-1]:
        count += 1

print(count)


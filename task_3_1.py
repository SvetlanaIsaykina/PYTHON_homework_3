# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи. 6 –>1 1 2 3 5 8

def find_fibo_numbers(count):
    fibo_nums = [0, 1]
    fibo_x = 0
    for el in range(n - 2):
        fibo_x = fibo_nums[-1] + fibo_nums[-2]
        fibo_nums.append(fibo_x)
    return fibo_nums

n = int(input('Введите число N: '))

data = open('fibonacci.txt', mode = 'a', encoding= 'utf-8')
data.write(f'{n} первых элементов последовательности Фибоначчи - {find_fibo_numbers(n)}' + '\n')
data.close
import random

def inputN(inputN):
    while True:
        try:
            Num = int(input(inputN))
            return Num
        except ValueError:
            print('Введите целое число')

N = inputN('Колличество элементов списка: ')

float_list = [round(random.random() * 10 , 2) for i in range(N)]
float_list2 = [round(i - int(i), 2) for i in float_list]

result = max(float_list2) - min(float_list2)

print(float_list2,' => ',result)
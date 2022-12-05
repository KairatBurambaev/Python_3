import random
import math
def inputN(inputN):
    while True:
        try:
            Num = int(input(f'{inputN}'))
            return Num
        except ValueError:
            print('Введите целое число')
float_list = []
float_list2 = []
N = int(input('Колличество элементов списка: '))
for i in range(N):
    i = round(random.random() * 10 , 2)
    float_list.append(i)
for elem in float_list:
    elem = round(elem - math.floor(elem), 2)
    float_list2.append(elem)
result = max(float_list2) - min(float_list2)
print(float_list2,' => ',result)
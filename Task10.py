import random
def inputlistN(inputlistN):
    while True:
        try:
            ListN = int(input(F'{inputlistN}'))
            ListN = list(range(1,ListN+1))
            random.shuffle(ListN)
            return ListN
        except ValueError:
            print('Нужно ввести число!')
    return ListN
N = inputlistN('Введите число N: ')
result = 0
for i in N:
    if N.index(i) % 2 == 1:
        result = result + i
print('Создан случайный списко из N эллементов: ',N,'\nСумма элементов на нечетных позиция: ',result)
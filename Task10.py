import random
def inputlistN(inputlistN):
    boolean = True
    while boolean:
        try:
            ListN = int(input(F'{inputlistN}'))
            ListN = list(range(1,ListN+1))
            random.shuffle(ListN)
            boolean = False
        except ValueError:
            print('Нужно ввести число!')
    return ListN
N = inputlistN('Введите число N: ')
result = 0
for i in N:
    if N.index(i) % 2 == 1:
        result = result + i
print(F'Создан случайный списко из N эллементов: {N}\nСумма элементов на нечетных позиция: ',result)
import random

def inputlistN(inputlistN):
    while True:
        try:
            ListN = int(input(inputlistN))
            return ListN
        except ValueError:
            print('Нужно ввести число!')

N = inputlistN('Введите число N: ')

listX = [random.randint(1,10) for i in range(N)]

def fu(i):
    return listX[i]*listX[len(listX)-i-1]

if len(range(N)) % 2:
    list_one = len(range(N))//2+1
else:
    list_one = len(range(N))//2

list_var = [fu(i) for i in range(list_one)]

print('список: ',listX,'\nПроизведение пар: ',list_var)
    
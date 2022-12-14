def inputN(inputN):
    while True:
        try:
            num = int(input(inputN))
            return num
        except ValueError:
            print('Введите целое число')

N = inputN('Введите число: ')
number = ''

while N > 0:
    if N % 2 == 0:
        number = str(0) + number
        N = N//2
    else:
        number = str(1) + number
        N = N//2

print(number)
def inputN(inputN):
    while True:
        try:
            Num = int(input(f'{inputN}'))
            return Num
        except ValueError:
            print('Введите целое число')
N = inputN('Введите число: ')
ist = []
while N > 0:
    if N % 2 == 0:
        ist.append(0)
        N = N//2
    else:
        ist.append(1)
        N = N//2
ist.reverse()
result =''
for elem in ist:
    result = result + str(elem)
print(result)

    
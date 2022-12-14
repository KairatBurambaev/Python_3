def inputK(inputK):
    while True:
        try:
            knum = int(input(inputK))
            return knum
        except ValueError:
            print('Введите число!')

k = inputK('Введите число: ')

fibo = [0,1]

for i in range (2, k+1):
    fibo.append(fibo[i-1]+fibo[i-2])

fibo_reverse = fibo.copy()
for i in range(1, k+1):
    if i % 2 == 0:
        fibo_reverse[i] = -1 * fibo[i]
fibo_reverse.reverse()

fibo = fibo_reverse[:-1] + fibo

print(fibo)
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
list_var = []
def prod(N):
    if len(N) % 2 != 0:
        list1 = len(N)//2 + 1 
    else:
        list1 = len(N)//2
    for i in range(list1):
        result = N[i]*N[len(N)-i-1] 
        list_var.append(result)
    print(F'список: {N}\nПроизведение пар: ,{list_var}')
N = inputlistN('Введите число N: ')
prod(N)
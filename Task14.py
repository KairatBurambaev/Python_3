def inputK(inputK):
    while True:
        try:
            knum = int(input(f'{inputK}'))
            knum = list(range(knum+1))
            return knum
        except ValueError:
            print('Введите число!')
k = inputK('Введите число: ')
new_list = []
new_list1 = []
for i in k:
    if i == k[0]:
        new_list.append(i)
    elif i == k[1]:
        new_list.append(i)
    else:
        i = new_list[i-1] + new_list[i-2]
        new_list.append(i)   
for x in new_list:    
    if new_list.index(x) % 2 !=0:
        new_list1.append(x)
    else:
        x = -x
        new_list1.append(x)
new_list1[2] = -1
new_list1.reverse() 
print(new_list1 + new_list[1:])
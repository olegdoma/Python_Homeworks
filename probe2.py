num = int(input())
for i in range(2, num):
    list_num = list[num % i]
    for j in list_num:
        if list_num[j] == 0:
            print('Число составное')
        else:
            print('Число простое')
    print(list_num)

#if a == 1:
#    print('Число простое')
#else:
#    print('Число составное')
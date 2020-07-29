stroka = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
stolbec = ['1', '2', '3', '4', '5', '6', '7', '8']
coord1 = input()
list_coord1 = list(coord1)
coord2 = input()
list_coord2 = list(coord2)
for i in stroka:
    for j in stolbec:
        if list_coord1[0] == i and list_coord1[1] == j:

            if (stroka.index(i) + stolbec.index(j)) % 2 == 0:
                cell1 = 1
            else:
                cell1 = 0

for i in stroka:
    for j in stolbec:
        if list_coord2[0] == i and list_coord2[1] == j:

            if (stroka.index(i) + stolbec.index(j)) % 2 == 0:
                cell2 = 1

            else:
                cell2 = 0

if cell1 == cell2:
    print('Клетки одинакового цвета')
else:
    print("Клектки не одинакового цвета")

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
def Print_table(td):
    col_width = []
    for x in range(len(td)):
        length = 0
        for y in range(len(td[0])):
            if len(td[x][y]) > length:
                length = len(td[x][y])
                # print(f'Текущая максимальная длина элемента {x}: - {length}')
        col_width.append(length)
        # print(f'Элемент списка col_width с индексом {x}: {col_width[x]}')
        # print(f'Текущий список col_width: {col_width}')
    # print(f'Длина списка td: {len(td)}')
    # print(f'Длина первого элемента списка td: {len(td[0])}')
    for a in range(len(td[0])):
        lst = ''
        for b in range(len(td)):
            if b < (len(td)):
                lst = lst + td[b][a].rjust(col_width[b] + 1)
        print(lst)


Print_table(table_data)

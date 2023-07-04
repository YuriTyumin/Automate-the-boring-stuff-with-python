# Программа рекурсивного обхода указанной папки и вывода информации и файлах,
# которые занимают размер, превышающий указанный.

import os
# import shutil
# import re

print('Введите путь к папке, в которой необходимо произвести поиск файлов')
source_dir = input()
print('Введите размер (в МБ) для файлов, превышение по размеру в которых необходимо найти')
input_size = input()
for folderName, subfolders, filenames in os.walk(source_dir):
    # print(f'\nТекущая папка: {folderName}')
    # print(f'Папки в текущей папке {folderName}: {subfolders}')
    # print(f'Список файлов в текущей папке {folderName}: {filenames}')
    for file in filenames:
        file_size = os.path.getsize(f'{folderName}\\{file}')
        if round(file_size/(1024*1024)) > int(input_size):
            print(f'Файл \'{folderName}\\{file}\' имеет размер:   {round(file_size/(1024*1024))}МБ')


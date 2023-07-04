#! python3
# Программа рекурсивного обхода указанной папки и выборочного копирования файлов с указанным расширением в указанную папку.

import os
import shutil
import re

print('Введите путь к папке, в которой необходимо произвести поиск файлов')
source_dir = input()
print('Введите расширение файлов, которые необходимо найти')
input_ext = input()
print('Введите путь к папке, в которую необходимо скопировать файлы')
target_dir = input()
ext_pattern = re.compile('.' + input_ext)
for folderName, subfolders, filenames in os.walk(source_dir):
    print(f'\nТекущая папка: {folderName}')
    print(f'Папки в текущей папке {folderName}: {subfolders}')
    print(f'Список файлов в текущей папке {folderName}: {filenames}')
    # print(f'{len(filenames)}')
    if len(filenames) > 0:
        for file in filenames:
            pattern_search = ext_pattern.search(file)
            try:
                if pattern_search.group() in file:
                    if os.path.exists(f'{target_dir}\\{file}') is True:
                        print(f'Файл \'{file}\' уже существует \n')
                    else:
                        print(f'Файл \'{folderName}\\{file}\' будет скопирован в папку: \'{target_dir}\'\n')
                        shutil.copy(f'{folderName}\\{file}', f'{target_dir}')
            except AttributeError:
                continue


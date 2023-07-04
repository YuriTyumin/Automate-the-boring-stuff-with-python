# Программа поиска и замены слов в тексте файла в рабочей папке.
# Результат работы программы выводится на экран (можно закомментировать этот "print" для экономии времени выполнения)
# и сохраняется в новый файл.
# Слова, вводимые для поиска и замены, чувствительны к регистру, поэтому, например "Все" != "все".
# Файлы для обработки необходимо поместить в папку с рабочей программой.

import re
import os
#import

print("Задайте пары искомого слова и слова для замены. Для завершения - нажмите Enter")
phrases = {}
while True:
    print('Введите искомое слово: ')
    word1 = input()
    print('Введите слово для замены: ')
    word2 = input()
    if (word1 and word2) != '':
        phrases[word1] = word2
    else:
        break
print(f'Заданные для коррекции пары слов:\n{phrases}')
file_lst = os.listdir(os.getcwd())
i = 0
for file in file_lst:
    if file != 'Replace_words.py':
        open_file = open(os.path.join(os.getcwd(), file))
        read_file = open_file.read()
        open_file.close()
        i += 1
        # print(f'\nФайл №{i}:\n{read_file}')
        for key in phrases:
            # print(f'{key}: {phrases[key]}')
            regexp = re.compile(f'{key}')
            x = regexp.search(read_file)
            while x.group() in read_file:
                # print(x.group())
                read_file = read_file.replace(f'{key}', f'{phrases[key]}')
            open_file = open(os.path.join(os.getcwd(), 'edited_' + file), 'w')
            open_file.write(read_file)
            open_file.close()
        print(f'\nФайл №{i}, исправленный:\n{read_file}')
    else:
        continue

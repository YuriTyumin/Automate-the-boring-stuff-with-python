import re


def strip(arg1, arg2):
    if arg2 == '':  # Удаление пробелов в начале и конце строки
        print(f'Исходная строка: \'{arg1}\'')
        while arg1[0] == ' ':
            arg1 = arg1[1:]
        # print(f'Удалены пробелы в начале строки: \'{arg1}\'')
        while arg1[-1] == ' ':
            arg1 = arg1[:-1]
        # print(f'Удалены пробелы в конце строки: \'{arg1}\'')
        print(f'Форматированная строка: \'{arg1}\'')
    else:   # Удаление заданных сочетаний символов
        print(f'Исходная строка: \'{arg1}\'')
        regexp = re.compile(f'{arg2}')
        mo = regexp.search(arg1)
        while mo.group() in arg1:
            arg1 = arg1.replace(f'{arg2}', '')
        print(f'Строка без символов: \'{arg2}\' \n \'{arg1}\'')


print('Введите исходный текст')
text_with_spaces = input()
print('Введите символы, которые необходимо удалить из исходного текста')
deleted_symbols = input()
strip(text_with_spaces, deleted_symbols)


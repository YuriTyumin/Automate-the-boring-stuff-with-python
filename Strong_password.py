import re


def strong_pass(input_password):
    if len(input_password) >= 8:
        print('Пароль не менее 7 символов')
        strong_password = re.compile(r'\d')
        mo = strong_password.search(input_password)
        try:
            if len(mo.group()) >= 1:
                print('В пароле есть минимум 1 цифра')
        except AttributeError:
            print(f'В пароле отсутствует хотя бы одна цифра')

        strong_password = re.compile(r'[A-Z]')
        mo = strong_password.search(input_password)
        try:
            if len(mo.group()) >= 1:
                print('В пароле есть минимум 1 буква в верхнем регистре')
        except AttributeError:
            print(f'В пароле отсутствует хотя бы одна буква верхнем регистре')

        strong_password = re.compile(r'[a-z]')
        mo = strong_password.search(input_password)
        try:
            if len(mo.group()) >= 1:
                print('В пароле есть минимум 1 буква в нижнем регистре')
        except AttributeError:
            print(f'В пароле отсутствует хотя бы одна буква в нижнем регистре')
    else:
        print('Пароль менее 8 символов')


print('Введите пароль для проверки сложности: ')
input_pass = input()
strong_pass(input_pass)


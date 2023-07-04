def collatz(number):
    if number >= 1:
        if (number % 2) == 0:
            print('Вы ввели четное число')
            return number // 2
        else:
            print('Вы ввели нечетное число')
            return (3 * number) + 1
    else:
        print('Вы ввели некорректное число')


print('Введите целое положительное число')
try:
    number = int(input())
    print(f'Результат выражения, который отдаёт функция: {collatz(number)}')
except ValueError:
    print('Вы ввели некорректную последовательность символов')
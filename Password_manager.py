#! python
import sys
from sys import argv
script_name, first_param = argv
dic = {'email': '23u9ijef-eqjib-934', 'web': '8u3t9834u-n-928u3u32ufh', 'blog': 'w893u192ix,9ie=19i,bg 71'}

if len(sys.argv) < 2:
    print('Формат использования: Имя_скрипта_Имя_сервиса')
    sys.exit()

if first_param in dic:
    print(f'{first_param}: {dic[first_param]}')
else:
    print('Такого имени сервиса нет в базе')
print('Программа завершена. Для выхода нажмите \'Enter\'')
if input() == '':
    sys.exit()

import time
import sys
import time

print('Чтобы начать отсчёт - нажмите <Enter>')
input()         # Нажатие <Enter> запускает отсчёт
print('Отсчёт начат')
start_time = time.time()
last_time = start_time
lap_num = 1
try:
    if True:
        input()
        # if KeyboardInterrupt != '':
        #     sys.exit()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f'Замер # {str(lap_num).rjust(3)}: {str(total_time).rjust(6)}' '  ' f'({str(lap_time).rjust(6)})', end='')
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    sys.exit()
    # print('\nГотово')
    # sys.exit()
except KeyError:
    sys.exit()



# print('Введите значение для таймера: ')
# timer = int(input())
# while timer > 0:
#     print(f'{timer}')
#     time.sleep(1)
#     timer -= 1
# print(f'{timer} - Time over')
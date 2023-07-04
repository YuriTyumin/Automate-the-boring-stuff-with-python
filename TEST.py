import csv
import json
import time
import datetime
import subprocess
import smtplib
import sys
import

# example_file = open('C:\\Users\\YuRick\\Desktop\\Automate the boring stuff with python\\automate_online-materials\\example.csv')
# example_reader = csv.reader(example_file)
# example_data = list(example_reader)
# for x in example_data:
#     print(x)

# output_file = open('output.csv', 'a', newline='')
# output_writer = csv.writer(output_file)
# output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
# output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# output_writer.writerow(['0.5', '1/3', '123', '3,14'])
# output_file.close()

# reader = open('CustomUI.JSON')
# test = reader.read()
# read_file = json.loads(test)
# print(f'Данные из исходного файла:\n{read_file}')
# reader.close()
# writer = open('CustomUI_edited.JSON', 'a', newline='')
# writer.write(str(read_file))
# writer.write('\n')
# writer.close()
# print(f'Данные записаны в новый файл')

# print(time.time())
# print(time.sleep())

# print(datetime.datetime.now())
# dt = datetime.datetime.now()
# print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, sep='_')
# print(dt.strftime('%Y-%m-%d %H:%M:%S'))

# subprocess.Popen('C:\Windows\WinSxS\wow64_microsoft-windows-calc_31bf3856ad364e35_10.0.19041.1_none_6a03b910ee7a4073\calc.exe')
# subprocess.Popen(['start', 'output.csv'], shell=True)

# smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_obj.ehlo()
# smtp_obj.starttls()
# smtp_obj.login('tyumin.yu@gmail.com', 'my_secret_password')
# smtp_obj.sendmail('tyumin.yu@gmail.com', ['t_yurick@rambler.ru', 'yurick@protonmail.com'],
#                   'Subject: Test\nTest python script mail')
# time.sleep(5)
# smtp_obj.quit()

print(sys.platform)


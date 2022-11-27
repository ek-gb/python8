# Тип интерфейса: CLI

from app.controller import ctrl
# from app.controller import db_sqlite3
# from app.controller import db_csv
# # from app.controller import db_mysql
from tkinter import filedialog

conn = None
csv_file_name = './import/tel.csv'

def init():
    c = input('''Выберите один из вариантов, что вы хотите сделать:
find - найти номер телефона по фамилии # Не реализовано
remove - удалить выбранные строки # Не реализовано
load - если вы хотите добавить данные в базу
''')
    print(f'Текущее состояние базы:\n{print_main_table()}')
    if c == 'find': btn_find_click() # Не реализовано
    elif c == 'remove': btn_remove_click() # Не реализовано
    elif c == 'load': btn_load_click()
    else: return

def btn_load_click(): # Добавила функцию
    c = input('''Выберите один из вариантов, откуда вы хотите добавить данные в базу:
con - из консоли
csv - из другого CSV-файла
''')
    if c == 'con':
        ctrl.load_from_console()
    elif c == 'csv':
        file_name = filedialog.askopenfilename(initialdir='./import') # Вызываем открытие проводника, чтобы выбрать файл. А есть ли другой способ?
        ctrl.load_from_csv(file_name)
    else:
        print('Вы ввели неверную команду.')
    print(f'Текущее состояние базы:\n{print_main_table()}')

def btn_find_click(): # Не реализовано
    print('# Не реализовано')
    pass

def btn_remove_click(): # Не реализовано
    print('# Не реализовано')
    pass

def print_main_table(str_pattern=''):
    return ctrl.get_data_from_database(str_pattern)
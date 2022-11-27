#!/usr/bin/python3

import sys
from app.controller import ctrl

g_mod = None # выбор графического интерфейса

d_mod = None # выбор 

def init():
    
    # Выбор графического интерфейса
    # 1 - GUI
    # 2 - CLI
    global g_mod

    # Выбор типа хранилища
    # 1 - SQLite
    # 2 - CSV
    # 3 - MySQL
    global d_mod

    for i in range(1, len(sys.argv)):
        match sys.argv[i]:
            case '-gui':
                g_mod = 1
            case '-cli': 
                g_mod = 2
            case '-sql':
                d_mod = 1
            case '-csv':
                d_mod = 2
            case '-msql':
                d_mod = 3
            case __:
                print('Неверный ввод параметров')
                return False

    if g_mod == None:
        c = input('Выберите графический интерфейс: gui (через графический интерфейс) или cli (через командную строку).\n')
        if c == 'gui': g_mod = 1
        elif c == 'cli': g_mod = 2
        else:
            print('Выбран неверный режим.')
            return False

    if d_mod == None:
        c = input('Выберите тип хранилища: s (SQLine), c (CSV) или m (MySQL).\n')
        if c == 's': d_mod = 1
        elif c == 'c': d_mod = 2
        # if db_mod == 'm': d_mod = 3 # Добавила строку, но пока закомметировала, как как msql не реализован до конца
        else:
            print('Выбран неверный режим.')
            return False
    
    return True

if init():
    ctrl.init(g_mod, d_mod)
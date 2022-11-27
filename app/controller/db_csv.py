# Модуль работы с CSV

from pathlib import Path
csv_path = None

def get_data(str_pattern) -> list[tuple[str,str,int]]: # Добавила эту функцию
    i = 1
    res = []
    with open(csv_path, mode = 'r', encoding = 'utf-8') as f:
        lst_str = f.read().splitlines()
        for elem_str in lst_str:
            elem: list = elem_str.split(',')
            elem.append(i)
            elem = tuple(elem)
            i += 1
            res.append(elem)
    return res

def push_data(lst_in): # Добавила эту функцию
    global csv_path
    csv_path = './data/tel.csv'
    with open(csv_path, mode = 'a', encoding = 'utf-8') as f:
        lst_in = map(lambda x: ','.join(x if x is not None else '') + '\n', lst_in)
        f.writelines(lst_in)
    
def create_table(): # Добавила эту функцию
    p = Path(csv_path)
    p.touch()

def remove_data(data):
    pass

def get_data_from_file(file_name) -> list[tuple[str,str]]: # Исправила эту функцию
    if file_name == None:
        return []
    try:
        with open(file_name, mode='r', encoding='utf-8') as f: # Добавила кодировку
            lst_str = f.read().splitlines()
        return [tuple(elem_str.split(',')) for elem_str in lst_str]
    except UnicodeDecodeError as e: # Добавила виды исключений
        print(e)
        raise e
    except UnicodeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

def init(): # Дописала эту функцию
    global csv_path
    csv_path = './data/tel.csv'
    create_table()

from tkinter import filedialog, ttk
from tkinter import *
from app.controller import ctrl

main_window = None
main_table = None

def init_main_window():
    
    w = main_window.winfo_screenwidth()
    h = main_window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200

    main_window.title('Телефонный справочник')
    main_window.geometry((f'700x400+{w}+{h}'))

def init_main_table(): 
    
    global main_table

    main_table = ttk.Treeview(main_window,show='headings',columns=['Наименование','Телефон'],name='table_main')
    main_table.column('Наименование',width=200,anchor=W)
    main_table.column('Телефон',width=100,anchor=E)
    main_table.heading('Наименование', text='Наименование',anchor=CENTER)
    main_table.heading('Телефон', text='Телефон',anchor=CENTER)
    
    # for i in range(10):
    #     main_table.insert('',i,values=(1,2))
    
    main_table.pack(expand=1,side=TOP,fill=BOTH)

def init_control_panel():

    top_panel = ttk.Frame(main_window,name='top_panel')
    top_panel.pack(side=TOP, fill=BOTH)


    field_find = ttk.Entry(top_panel,width=50, name='entry_find')
    field_find.pack(side=LEFT,padx=5,pady=5)

    btn_find = ttk.Button(top_panel,text='Найти',command=btn_find_click)
    btn_find.pack(side=LEFT,pady=5)

    btn_remove = ttk.Button(top_panel,text='Удалить',command=btn_remove_click)
    btn_remove.pack(side=LEFT,padx = 10, pady=5)

    btn_load = ttk.Button(top_panel,text='Загрузить',command=btn_load_click)
    btn_load.pack(side=LEFT,pady=5)

def fill_main_table(str_pattern=''):

    global main_table
    i = 0
    data = ctrl.get_data_from_database(str_pattern)
    print(data)
    for elem in data:
        main_table.insert('',i,values=elem)
        i += 1

def init():

    global main_window

    main_window = Tk()

    init_main_window()
    init_control_panel()
    init_main_table()
    fill_main_table()
    main_window.mainloop()

def btn_find_click():
   
    str_query = main_window.children['top_panel'].children['entry_find'].get()
    if str_query == '':
        clean_main_table()
        fill_main_table()
    else:
        clean_main_table()
        fill_main_table(str_query)

def btn_load_click():
   
    file_name = filedialog.askopenfilename(initialdir='./import')
    ctrl.load_from_csv(file_name)
    clean_main_table()
    fill_main_table()

def btn_remove_click():

    data = tuple(main_table.item(main_table.focus())['values'])
    if data == ():
        return
    ctrl.remove_data_from_database(data)
    clean_main_table()
    fill_main_table()

def clean_main_table():
    for i in main_table.get_children():
        main_table.delete(i)

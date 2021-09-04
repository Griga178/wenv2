import funcs_data

message = input('Для вывода всего списка товаров "a":\n'
                'Для списка элементов внутри системы "b"\n'
                'Для добавление новой системы "с"\n'
                'Для добавление элемента в состав системы "d"\n'
                'Для построениея карты систем "e"\n')


file_name = 'data/systems.csv'
file_name2 = 'data/links.csv'

if message == 'a':
    list = funcs_data.print_all(file_name)
    for el in list:
        print(el)
elif message == 'b':
    list2 = funcs_data.print_all(file_name)
    for el in list2:
        print(el)
    new_mes = input('Выберете номер системы\n')
    list = funcs_data.print_all(file_name2)
    for el in list:
        if el[0] == new_mes:
            #print(f'В {el[1]} входят следующие элементы:')
            for ell in list2:
                if ell[0] == el[1]:
                    print(ell[1])
elif message == 'c':
    new_sys = input('Введите имя: \n')
    print(new_sys)
elif message == 'd':
    pass

elif message == 'e':
    pass
    '''
    Компьютер:
        Процессор:
            Ядро:
                Частота запросов?
            Память:
                Объем
                Частота
        Оперативная память:
            Частота
            Объем
    '''


# тут я закончил и решил перейти на sqlite3

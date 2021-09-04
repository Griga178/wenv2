import csv



def print_all(file_name):
    list = []
    with open(file_name, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ";")
        for row in reader:
            list.append(row)
        return list

def add_new_sys(file_name, name):
    with open(file_name, 'a') as file:
        for row in reader:
            list.append(row)
        return list # тут я закончил и решил перейти на sqlite3

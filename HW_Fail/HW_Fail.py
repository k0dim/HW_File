from operator import itemgetter
import os

# Задача №1

ROAD = os.getcwd()
DIR_NAME = 'HW_Fail'
FILE_NAME = 'recipes.txt'
full_path = os.path.join(ROAD, DIR_NAME, FILE_NAME)

with open(full_path) as file:
    cook_book = {}
    for line in file:
        clean_line = line.strip()
        list_ingredients = []
        for item in range(int(file.readline())):
            ingredients_dict = {}
            name, quantity, measure = file.readline().split(' |')
            ingredients_dict['ingredient_name'] = name.strip(' \n')
            ingredients_dict['quantity'] = int(quantity.strip(' \n'))
            ingredients_dict['measure'] = measure.strip(' \n')
            list_ingredients.append(ingredients_dict)
        cook_book[clean_line] = list_ingredients
        file.readline()
# print(cook_book)

# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    ingredients_dict = {}
    for key, value in cook_book.items():
        if key in dishes:
            for ingredient in value:
                name = ingredient['ingredient_name']
                ingredients['quantity'] = ingredient['quantity'] * int(person_count)
                ingredients['measure'] = ingredient['measure']
                ingredients_dict.update({name:ingredients})
    print(ingredients_dict)
    return  
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задача №3

def read_file(num_file):
    PATH = os.getcwd()
    DIR_NAME = 'HW_Fail'
    FILE = 'sorted'
    FILE_NAME = f'{num_file}'
    full_path = os.path.join(PATH, DIR_NAME, FILE, FILE_NAME)

    with open(full_path) as file:
        text = file.read()
        return text

def read_line_file(num_file):
    PATH = os.getcwd()
    DIR_NAME = 'HW_Fail'
    FILE = 'sorted'
    FILE_NAME = f'{num_file}.txt'
    full_path = os.path.join(PATH, DIR_NAME, FILE, FILE_NAME)

    with open(full_path) as file_:
        count_line = 1
        for line in  file_:
            if '\n' in line:
                count_line += 1
    return count_line

def count_line():
    dict_line_file = {}
    for file_all in range(1, int(input('Укажите колличество файлов: '))+1):
        dict_line_file[f'{file_all}.txt'] = read_line_file(f'{file_all}')
    sorted_file = dict(sorted(dict_line_file.items(), key=itemgetter(-1)))
    return sorted_file

def write_new_file():
    PATH = os.getcwd()
    DIR_NAME = 'HW_Fail'
    FILE = 'sorted'
    FILE_NAME = 'result.txt'
    full_path = os.path.join(PATH, DIR_NAME, FILE, FILE_NAME)

    with open(full_path, 'w') as file:
        count_dict = count_line()
        for name, count in (count_dict.items()):
            file.write(f'{name} \n')
            file.write(f'{count} \n')
            file.write(f'{read_file(name)} \n')

    with open(full_path, 'r') as file:
        print('В файле было записано следующие: \n')
        print(file.read())

    return
# write_new_file()

def home_wokr():
    work = int(input('Укажите номер задания: '))
    if work == 1:
        print(cook_book)
    elif work == 2:
        eat = input('Укажите список блюд: ')
        people = input('Укажите колличество персон: ')
        get_shop_list_by_dishes(eat, people)
    elif work == 3:
        write_new_file()
    return

home_wokr()
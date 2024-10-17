import csv
import random

DATASET_PATH = 'books.csv'
OUT_PATH = 'out.txt'

def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    return title

def get_objects(file, title):
    reader = csv.DictReader(file, title, delimiter=';', quotechar='"')
    list = []
    for line in reader:
        list.append(line)
    return list

if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        title = get_title(dataset)
        books = get_objects(dataset, title)
        
        ans = 0
        for element in books:
            if len(element['Название']) > 30:
                ans += 1
        print('Количество записей, y которых в поле Название '
              +'строка длиннее 30 символов:', ans)
        
        author = input('Введите имя автора: ')
        print('Найденные записи:')
        counter = 1
        years = list()
        for element in books:
            date, time = element['Дата поступления'].split()
            year = date[-4:]
            years.append(year)
            if (((author in element['Автор']) 
                or (author in element['Автор (ФИО)']))
                and (year in ['2014', '2016', '2017'])):
                print(f'  {counter}. {element['Автор (ФИО)']} '
                      +f'"{element['Название']}", {year}')
                counter += 1

        with open(OUT_PATH, 'w') as out:
            rand_list = set()
            while len(rand_list) < 20:
                rand_number = random.randint(0, len(books))
                rand_list.add(rand_number)
                if books[rand_number]['Автор (ФИО)'] == '':
                    out.write(f'{books[rand_number]['Название']}'
                              +f'- {years[rand_number]}\n')
                else:
                    out.write(f'{books[rand_number]['Автор (ФИО)']}. '
                              +f'{books[rand_number]['Название']} - '
                              +f'{years[rand_number]}\n')
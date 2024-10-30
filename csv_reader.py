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
        
        author_filter = input('Введите имя автора: ')
        print('Найденные записи:')
        counter = 1
        years = list()
        years_filter =  ['2014', '2016', '2017']
        for element in books:
            date, time = element['Дата поступления'].split()
            year = date[-4:]
            years.append(year)
            author = element['Автор']
            author_fio = element['Автор (ФИО)']
            book_name = element['Название']
            if (((author_filter in author) 
                or (author_filter in author_fio))
                and (year in years_filter)):
                print(f'  {counter}. {author_fio} '
                      +f'"{book_name}", {year}')
                counter += 1

        with open(OUT_PATH, 'w') as out:
            rand_list = set()
            counter = 0
            while counter < 20:
                rand_number = random.randint(0, len(books))
                author_fio = books[rand_number]['Автор (ФИО)']
                book_name = books[rand_number]['Название']
                if not(rand_number in rand_list):
                    if author_fio == '':
                        counter = len(rand_list) + 1
                        out.write(f'{counter}. '
                                  +f'"{book_name}" - '
                                  +f'{years[rand_number]}\n')
                        rand_list.add(rand_number)
                    else:
                        counter = len(rand_list) + 1
                        out.write(f'{counter}. '
                                  +f'{author_fio}. '
                                  +f'"{book_name}" - '
                                  +f'{years[rand_number]}\n')
                        rand_list.add(rand_number)
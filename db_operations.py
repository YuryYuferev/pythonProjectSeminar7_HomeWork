def get_input(req):
    answer = []
    for i in req:
        print(f'\nВведите {i}:')
        answer.append(input())
    return answer


def get_add():
    request = ['Фамилию:', 'Имя:', 'Отчество:', 'номер телефона:', 'принадлежность телефона (рабочий/личный):',
               'тип телефона (сотовый/стационарный):', 'должность:']
    data = get_input(request)
    with open('people.csv', 'a') as file:
        file.writelines(
            f'{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}\n')


def get_remove():
    request = ['Введите фамилию для удалению:']
    data = (','.join((''.join((get_input(request)))).split(' '))).split(',')
    db_remove = []
    db_new = []
    with open('people.csv', 'r') as file:
        for line in file:
            match = True
            for key in data:
                if key not in line:
                    match = False
            if match:
                db_remove.append(line.replace('\n', ''))
            else:
                db_new.append(line.replace('\n', ''))
    print('По указанным параметрам подобран абонент:')
    [print(line) for line in db_remove]
    if input('Нажмите Y, если вы хотите удалить указанного абонента:\n') == 'Y':
        with open('people.csv', 'w') as file:
            [file.writelines(f'{line}\n') for line in db_new]


def get_find():
    request = ['Введите фамилию для поиска:']
    data = (','.join((''.join((get_input(request)))).split(' '))).split(',')
    db_remove = []
    with open('people.csv', 'r') as file:
        for line in file:
            match = True
            for key in data:
                if key not in line:
                    match = False
            if match:
                db_remove.append(line.replace('\n', ''))
    print('По указанным параметрам подобран абонент:')
    [print(line) for line in db_remove]




# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = {}

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

for key, value in names.items():
    print(f'{key}: {value}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = {}

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

common = 0
for key, value in names.items():
    if value > common:
        common = value
        common_name = key
print(f'Самое частое имя среди учеников: {common_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

names = {}


def count_names():
    for student in classes:
        if student['first_name'] not in names.keys():
            names[student['first_name']] = 1
        else:
            names[student['first_name']] += 1

    common = 0
    for key, value in names.items():
        if value > common:
            common = value
            common_name = key
    return common_name


n = 0
for classes in school_students:
    n += 1
    common_name = count_names()
    print(f'Самое частое имя в классе {n}: {common_name}')
    names.clear()


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def check_gender(students):
    female = 0
    male = 0
    for student in students:
        if is_male[student['first_name']] is False:
            female += 1
        if is_male[student['first_name']] is True:
            male += 1
    return [female, male]


for classes in school:
    gender = check_gender(classes["students"])
    print(f'Класс {classes["class"]}: девочки {gender[0]}, мальчики {gender[1]}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


def check_gender(students):
    female = 0
    male = 0
    for student in students:
        if is_male[student['first_name']] is False:
            female += 1
        elif is_male[student['first_name']] is True:
            male += 1
    return [female, male]


for classes in school:
    gender = check_gender(classes["students"])
    if gender[0] < gender[1]:
        print(f'Больше всего мальчиков в классе {classes["class"]}')
    elif gender[0] > gender[1]:
        print(f'Больше всего девочек в классе {classes["class"]}')

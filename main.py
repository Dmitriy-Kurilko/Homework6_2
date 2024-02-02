import random

def get_list_of_words(user_quantity):
    '''
    Получает список слов, которые рандомно отсортированы.
    '''
    res = []
    with open('words.txt', 'r') as file:
        lst = [i.rstrip('\n') for i in file]
        for i in range(user_quantity):
            res.append(lst[random.randint(0, 7)])
    return res


def letters_mix(word):
    '''
    Перемешивает буквы в слове.
    '''
    n = list(word)
    random.shuffle(n)
    return n


def get_results(user_name):
    '''
    Подсчитывает, сколько было сыграно игр пользователем и его максимальное кол-во очков(рекорд).
    '''
    quantity_games = 0
    max_points = 0
    with open('history.txt', 'r') as file:
        lst = [i.rstrip('\n') for i in file]
        if len(lst) == 0:return [0, 0]  # Проверка на то, что файл не пустой
        for line in lst:
            name, points = line.split()
            if name == user_name:
                if int(points) > int(max_points):
                    max_points = points
                quantity_games += 1

    return [quantity_games, max_points]


def write_new_dates(user_name, points):
    '''
    Записывает новые данные в файл.
    '''
    with open('history.txt', 'a') as file:
        file.write(f'{user_name} {points}\n')


def write_results():
    '''
    Выводит, сколько было сыграно игр пользователем и его максимальное кол-во очков(рекорд).
    '''
    if get_results(user_name)[0] == 0:  # Если файл пустой, то условие == True
        print(f'Всего игр сыграно: {1}')
        print(f'Максимальный рекорд: {points}')
        exit()
    quantity_games, max_points = get_results(user_name)

    if int(points) > int(max_points):
        print(f'Всего игр сыграно: {quantity_games}')
        print(f'Максимальный рекорд: {points}')
    else:
        print(f'Всего игр сыграно: {quantity_games}')
        print(f'Максимальный рекорд: {max_points}')

# Начало кода


user_name = input('Привет! Введи свое имя: ').lower()            # Константа
user_quantity = int(input('Сколько слов хотите угадать? '))      # Константа
random_words = get_list_of_words(user_quantity)                  # Константа
points = 0

for i in random_words:
    print(f'Угадайте слово: {"".join(letters_mix(i))}')
    user_input = input().lower()
    if user_input == i:
        print('Верно! Вы получаете 10 очков.')
        points += 10
    else:
        print(f'Неверно! Верный ответ – {i}.')

write_new_dates(user_name, points)
write_results()
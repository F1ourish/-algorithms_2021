"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint


def guess_a_num(takes, var):
    print(f'{takes} попытка.')
    user_num = int(input('Угадайте загаданное мной число от 0 до 100: '))
    if user_num == var or takes == 10:
        if user_num == var:
            print(f'Вы угадали число {var}, потратив {takes} попытки(ок). Поздравляю!')
        else:
            print('К сожалению, у вас закончились попытки')
    else:
        if user_num > var:
            print('Ваше число больше загаданного, попробуйте ещё раз.')
        else:
            print('Ваше число меньше загаданного, попробуйте ещё раз.')
        return guess_a_num(takes + 1, var)


guess_a_num(1, randint(0, 100))

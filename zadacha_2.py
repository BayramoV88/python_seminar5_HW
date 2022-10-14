# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def input_dat(name):
    x = int(input(f'{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    if x < 1 or x > 28:
        x = int(input(f'{name}, введите корректное количество конфет: '))
    return x


def p_print(name, k, counter, total):
    print(f'{name} взял {k} конфет, теперь у него их {counter}. На столе осталось {total} конфет.')


player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
total = int(input('Какое количество конфет на столе: '))
flag = randint(0, 2)
if flag:
    print(f'Первый ходит {player_1}')
else:
    print(f'Первый ходит {player_2}')

counter_1 = 0
counter_2 = 0

while total > 28:
    if flag:
        k = input_dat(player_1)
        counter_1 += k
        total -= k
        flag = False
        p_print(player_1, k, counter_1, total)
    else:
        k = input_dat(player_2)
        counter_2 += k
        total -= k
        flag = True
        p_print(player_2, k, counter_2, total)

if flag:
    print(f'Выиграл {player_1}, все {counter_2} конфет оппонента  достаются ему.')
else:
    print(f'Выиграл {player_2}, все {counter_1} конфет оппонента  достаются ему.')
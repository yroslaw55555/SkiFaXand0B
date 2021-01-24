# !/usr/bin/env python

L = [[i+j for j in range(4)] for i in range(4)]

GameWin = ''
past_tur = ''

for i in range(len(L)):
    for j in range(len(L[i])):
         if i and j:
              L[i][j] = '-'
         elif not(i and j):
              L[i][j] -= 1
         if  not i and not j:
              L[i][j] = ' '


def show_game ():
    for i in L:
        print(" ".join(map(str,i)))



def tir_in_L ():
    tir = 0
    for i in L:
        if '-' in i:
            tir += 1
    return tir

def win():
    if (L[1][1]==L[2][2]==L[3][3]) or (L[1][3]==L[2][2]==L[3][1]):
        if L[2][2] != '-':
            GameWin = str(L[2][2])
    if (L[1][1]==L[1][2]==L[1][3]) or (L[1][1]==L[2][1]==L[3][1]):
        if L[1][1] != '-':
            GameWin = str(L[1][1])
    if L[1][2]==L[2][2]==L[3][2] or L[2][1]==L[2][2]==L[2][3]:
        if L[2][2] != '-':
            GameWin = str(L[2][2])
    if L[3][1]==L[3][2]==L[3][3] or L[1][3]==L[2][3]==L[3][3]:
        if L[3][3] != '-':
            GameWin = str(L[3][3])
    return GameWin

while tir_in_L ():
    show_game ()
    yx=list(input('Введите через пробел координаты x и у а затем символ:').lower().split())
    while not(int(yx[0])+1 and int(yx[1])+1) or (((int(yx[0])+1) > 3) or ((int(yx[1])+1) > 3)):
        yx=list(input('y и x не могут быть меньше 0 или больше 2:').lower().split())
    while L[int(yx[0])+1][int(yx[1])+1] != '-':
        yx=list(input('Эта клетка занята:').split())
    while  yx[2]!='x' and yx[2]!='0':
        print ('Это игра крестики нолики...')
        yx=list(input('Введите через пробел координаты x и у а затем символ:').lower().split())
    while past_tur == yx[2]:
        print ('Сейчас не твой ход', past_tur)
        yx=list(input('Введите через пробел координаты x и у а затем символ:').lower().split())
    L[int(yx[0])+1][int(yx[1])+1] = yx[2]

    win()
    if GameWin != '':
        break
    past_tur = str(yx[2])

show_game ()

if GameWin == '':
    GameWin = 'Дружба!!!'

print('Игра закончена выйграл: ', GameWin,'!!!')
input()

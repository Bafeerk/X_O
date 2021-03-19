import tkinter as tk
from model import *
field = [
         [0, '1', '2', '3'],
         [1, '-', '-', '-'],
         [2, '-', '-', '-'],
         [3, '-', '-', '-']
        ]

def computer_begins():
    f = open('debut.txt', 'r')
    begin = f.read(1)
    print(begin)
    if begin == '1':
        field[2][2] = 'O'
        play_zone.create_oval(100, 100, 200, 200)
    f.close()

def statistics():
    f = open('statistic.txt', 'r')
    number_of_birds = f.readline()
    f.close()
    number_of_birds = int(number_of_birds)
    number_of_birds += 1
    number_of_birds = str(number_of_birds)
    f = open('statistic.txt', 'w')
    f.write(number_of_birds)
    f.close()
    

def draw_O(i, j, x_1, y_1, x_2, y_2):
    """
        Изменяет массив field и рисует окружность на указанных кординатах
        Получает натуральные числа. i, j от 1 до 3.
    """
    print('draw_0')
    field[i][j] = 'O'
    play_zone.create_oval(x_1, y_1, x_2, y_2)

def computer(field):
    """
        Имитирует ход компьютера, ставит 'O' на свободное место '-'
        Принимает массив
        Ничего не возвращает
    """
    row = computer_cheks_rows(field, 'X')
    col = computer_cheks_columns(field, 'X')
    dia = computer_cheks_diagonals(field, 'X')
    row_1 = computer_cheks_rows(field, 'O')
    col_1 = computer_cheks_columns(field, 'O')
    dia_1 = computer_cheks_diagonals(field, 'O')
## Проверяет свободен ли центр    
    if is_center_free(field):
        field[2][2] = 'O'
        play_zone.create_oval(100, 100, 200, 200)
## Проверяет наличие двух 'O' подряд
    elif row_1 == '11' or col_1 == '11' or dia_1 == '11':
        print(11)
        draw_O(1, 1, 0, 0, 100, 100)
    elif row_1 == '12' or col_1 == '12':
        print(12)
        draw_O(1, 2, 100, 0, 200, 100)
    elif row_1 == '13' or col_1 == '13' or dia_1 == '13':
        print(13)
        draw_O(1, 3, 200, 0, 300, 100)
    elif row_1 == '21' or col_1 == '21':
        print(21)
        draw_O(2, 1, 0, 100, 100, 200)
    elif row_1 == '22' or col_1 == '22' or dia_1 == '22':
        print(22)
        draw_O(2, 2, 100, 100, 200, 200)
    elif row_1 == '23' or col_1 == '23':
        print(23)
        draw_O(2, 3, 200, 100, 300, 200)
    elif row_1 == '31' or col_1 == '31' or dia_1 == '31':
        print(31)
        draw_O(3, 1, 0, 200, 100, 300)
    elif row_1 == '32' or col_1 == '32':
        print(32)
        draw_O(3, 2, 100, 200, 200, 300)
    elif row_1 == '33' or col_1 == '33' or dia_1 == '33':
        print(33)
        draw_O(3, 3, 200, 200, 300, 300)
## Проверяет наличие дух 'X' подряд
    elif row == '11' or col == '11' or dia == '11':
        print(11)
        draw_O(1, 1, 0, 0, 100, 100)
    elif row == '12' or col == '12':
        print(12)
        draw_O(1, 2, 100, 0, 200, 100)
    elif row == '13' or col == '13' or dia == '13':
        print(13)
        draw_O(1, 3, 200, 0, 300, 100)
    elif row == '21' or col == '21':
        print(21)
        draw_O(2, 1, 0, 100, 100, 200)
    elif row == '22' or col == '22' or dia == '22':
        print(22)
        draw_O(2, 2, 100, 100, 200, 200)
    elif row == '23' or col == '23':
        print(23)
        draw_O(2, 3, 200, 100, 300, 200)
    elif row == '31' or col == '31' or dia == '31':
        print(31)
        draw_O(3, 1, 0, 200, 100, 300)
    elif row == '32' or col == '32':
        print(32)
        draw_O(3, 2, 100, 200, 200, 300)
    elif row == '33' or col == '33' or dia == '33':
        print(33)
        draw_O(3, 3, 200, 200, 300, 300)
## Ставит 'O' на первую попавшуюся пустую клетку
    else:
        global free
        free = find_free_cells(field)
        if free == '11':
            print(11)
            play_zone.create_oval(0, 0, 100, 100)
        elif free == '12':
            print(12)
            play_zone.create_oval(100, 0, 200, 100)
        elif free == '13':
            print(13)
            play_zone.create_oval(200, 0, 300, 100)
        elif free == '21':
            print(21)
            play_zone.create_oval(0, 100, 100, 200)
        elif free == '22':
            print(22)
            play_zone.create_oval(100, 100, 200, 200)
        elif free == '23':
            print(23)
            play_zone.create_oval(200, 100, 300, 200)
        elif free == '31':
            print(31)
            play_zone.create_oval(0, 200, 100, 300)
        elif free == '32':
            print(32)
            play_zone.create_oval(100, 200, 200, 300)
        elif free == '33':
            print(33)
            play_zone.create_oval(200, 200, 300, 300)
        print('Ничего не выполнилось')

def draw_X(event, a1, b1, a2, b2):
    """
        Рисует крестик
    """
    play_zone.create_line(a1 + 10, b1 + 10, a2 - 10, b2 - 10)
    play_zone.create_line(a1 + 10, b2 - 10, a2 - 10, b1 + 10)

def is_cell(event):
    """
        Показывает, где игрок произвел клик мышкой
        Принимает event
        Возвращает bool или int
    """
    x = event.x
    y = event.y
    if x > 0 and x < 100 and y > 0 and y < 100:
        return 11
    elif x > 100 and x < 200 and y > 0 and y < 100:
        return 12
    elif x > 200 and x < 300 and y > 0 and y < 100:
        return 13
    elif x > 0 and x < 100 and y > 100 and y < 200:
        return 21
    elif x > 100 and x < 200 and y > 100 and y < 200:
        return 22
    elif x > 200 and x < 300 and y > 100 and y < 200:
        return 23
    elif x > 0 and x < 100 and y > 200 and y < 300:
        return 31
    elif x > 100 and x < 200 and y > 200 and y < 300:
        return 32
    elif x > 200 and x < 300 and y > 200 and y < 300:
        return 33
    return False

def play(event):
    if is_cell(event) == 11 and field[1][1] == '-':
        draw_X(event, 0, 0, 100, 100)
        field[1][1] = 'X'
    elif is_cell(event) == 12 and field[1][2] == '-':
        draw_X(event, 100, 0, 200, 100)
        field[1][2] = 'X'
    elif is_cell(event) == 13 and field[1][3] == '-':
        draw_X(event, 200, 0, 300, 100)
        field[1][3] = 'X'
    elif is_cell(event) == 21 and field[2][1] == '-':
        draw_X(event, 0, 100, 100, 200)
        field[2][1] = 'X'
    elif is_cell(event) == 22 and field[2][2] == '-':
        draw_X(event, 100, 100, 200, 200)
        field[2][2] = 'X'
    elif is_cell(event) == 23 and field[2][3] == '-':
        draw_X(event, 200, 100, 300, 200)
        field[2][3] = 'X'
    elif is_cell(event) == 31 and field[3][1] == '-':
        draw_X(event, 0, 200, 100, 300)
        field[3][1] = 'X'
    elif is_cell(event) == 32 and field[3][2] == '-':
        draw_X(event, 100, 200, 200, 300)
        field[3][2] = 'X'
    elif is_cell(event) == 33 and field[3][3] == '-':
        draw_X(event, 200, 200, 300, 300)
        field[3][3] = 'X'
    else:
        print('Промазал')
        return 
        
    if is_win(field, 'X'):
        draw_field(field)
        print('You win')
        f = open('debut.txt', 'w')
        f.write('0')
        f.close()
        statistics()
        win.destroy()
        return
        
    computer(field)

    if is_win(field, 'O'):
       draw_field(field)
       print('Поздравляем, вы проиграли')
       f = open('debut.txt', 'w')
       f.write('1')
       f.close()
       statistics()
       win.destroy()

    if nobody_win(field) == False:
        print('Ничья')
        statistics()
        win.destroy()

    draw_field(field)
    

win = tk.Tk()
win.title("Крестики - нолики")

play_zone = tk.Canvas(win, width = 300, height = 300, bg = "#99ffff")
play_zone.pack()

play_zone.create_line(0, 100, 300, 100, width = 1)
play_zone.create_line(0, 200, 300, 200, width = 1)
play_zone.create_line(100, 0, 100, 300, width = 1)
play_zone.create_line(200, 0, 200, 300, width = 1)

win.bind('<Button-1>', play)

computer_begins()


win.mainloop()

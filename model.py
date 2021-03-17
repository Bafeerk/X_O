def draw_field(field):
    """
        Функция рисует поле
        Принимает список, ничего не возвращает
    """
    i = 0
    while i < len(field):
        print(field[i])
        i = i + 1

def check_rows(field, symbol):
    """
        Проверяет ряды массива на наличие трех идущих подряд 'X' или 'O'
        Принимает массив и строку ('X' или 'O')
        Возвращает bool
    """
    if field[1][1] + field[1][2] + field[1][3] == symbol * 3:
        print('check_rows, 1')
        return True
    elif field[2][1] + field[2][2] + field[2][3] == symbol * 3:
        return True
    elif field[3][1] + field[3][2] + field[3][3] == symbol * 3:
        return True
    else:
        return False

def check_columns(field, symbol):
    """
        Проверяет столбцы массива на наличие трех идущих подряд 'X' или 'O'
        Принимает массив и строку ('X' или 'O')
        Возвращает bool
    """
    if field[1][1] + field[2][1] + field[3][1] == symbol * 3:
        print('check_columns, 1')
        return True
    elif field[1][2] + field[2][2] + field[3][2] == symbol * 3:
        return True
    elif field[1][3] + field[2][3] + field[3][3] == symbol * 3:
        return True
    else:
        return False

def check_diagonals(field, symbol):
    """
        Проверяет диагонали массива на наличие трех идущих подряд 'X' или 'O'
        Принимает массив и строку ('X' или 'O')
        Возвращает bool
    """    
    if field[1][1] + field[2][2] + field[3][3] == symbol * 3:
        return True
    elif field[3][1] + field[2][2] + field[1][3] == symbol * 3:
        return True
    else:
        return False

def is_win(field, symbol):
    """
        Проверяет поле на наличие трех идущих подряд 'X' или 'O'
        Получает массив поля, и строку ('X' или 'O')
        Возвращает bool
    """
    if check_rows(field, symbol):
        return True
    elif check_columns(field, symbol):
        return True
    elif check_diagonals(field, symbol):
        return True
    else:
        return False

def computer_cheks_rows(field, symbol):
    """
        Проверяет строки на наличие в низ двух 'XX' или 'O' и '-'
        Принимает массив и строку ('X', 'O')
        Возвращает bool
    """
    print('I checks rows')
    i = 1
    while i < 4:
        if field[i][1] + field[i][2] + field[i][3] == '-' + symbol * 2:
            print('computer checks, 1')
            x = str(i) + '1'
            print(type(x))
            return x
        elif field[i][1] + field[i][2] + field[i][3] == symbol + '-' + symbol:
            x = str(i) + '2'
            return x
        elif field[i][1] + field[i][2] + field[i][3] == symbol * 2 + '-':
            x = str(i) + '3'
            print(type(x))
            print(x)
            return x
        i += 1
    return False

def computer_cheks_columns(field, symbol):
    """
        Проверяет столбцы на наличие в низ двух 'XX' или 'O' и '-'
        Принимает массив и строку ('X', 'O')
        Возвращает bool
    """
    print('Hi, I checks columns')
    i = 1
    while i < 4:
        if field[1][i] + field[2][i] + field[3][i] == '-' + symbol * 2:
            print('computer checks, 1')
            x = '1' + str(i)
            return x
        elif field[1][i] + field[2][i] + field[3][i] == symbol + '-' + symbol:
            x = '2' + str(i)
            return x
        elif field[1][i] + field[2][i] + field[3][i] == symbol * 2 + '-':
            x = '3' + str(i)
            return x
        i += 1
    return False

def computer_cheks_diagonals(field, symbol):
    """
        Проверяет диагонали на наличие в низ двух 'XX' или 'O' и '-'
        Принимает массив и строку ('X', 'O')
        Возвращает bool
    """
    print('Hi, I checks disgonals')
    if field[1][1] + field[2][2] + field[3][3] == '-' + symbol * 2:
        return '11'
    elif field[1][1] + field[2][2] + field[3][3] == symbol + '-' + symbol:
        return '22'
    elif field[1][1] + field[2][2] + field[3][3] == symbol * 2 + '-':
        return '33'
    elif field[3][1] + field[2][2] + field[1][3] == '-' + symbol * 2:
        return '31'
    elif field[3][1] + field[2][2] + field[1][3] == symbol + '-' + symbol:
        return '22'
    elif field[3][1] + field[2][2] + field[1][3] == symbol * 2 + '-':
        return '13'
    else:
        return False

def is_center_free(field):
    """
        Проверяет свободен ли центр игрового поля
        Принимает массив
        Возвращает bool
    """
    if field[2][2] == '-':
        return True
    else: return False

def find_free_cells(field):
    """
        Ищет пустые ячейки и вставляет туда 'O'
        Принимает массив
        Ничего не возвращает
    """
    i = 1
    while i < 4:
        j = 1
        while j < 4:
            if field[i][j] == '-':
                field[i][j] = 'O'
                x = str(i) + str(j)
                return x
            j += 1
        i += 1

def nobody_win(field):
    """
        Проверяет массив на отсутствие в нем '-'
        Принимает массив
        Возвращает bool
    """
    i = 1
    while i < 4:
        j = 1
        while j < 4:
            if field[i][j] == '-':
                return True
            j += 1
        i += 1
    return False

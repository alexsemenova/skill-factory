print("---------------------------------------")
print("Добро пожаловать в игру крестики-нолики")
print("---------------------------------------")
print("Для ввода координат:")
print("x - строка")
print("y - столбец")
print("---------------------------------------")
board = [[" "] * 3 for i in range(3)]


def game_board():
    """Функция для вывода игрового поля"""
    print()
    print("    | 0 | 1 | 2 | ")
    print("   -------------- ")
    for i, value in enumerate(board):
        print(f"  {i} | {' | '.join(value)} |")
        print("   ------------- ")
    print()


def take_coordinates():
    """Фукнция для ввода координат и проверки требований к координатам"""
    while True:
        coordinates = input('Введите две координаты ').split()

        if len(coordinates) != 2:
            print("Введите две координаты")
            continue

        x, y = coordinates

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите два целых числа")
            continue

        x, y = int(x), int(y)

        if not (0 <= x <= 2) or not (0 <= y <= 2):
            print("Введенные координаты вне поля")
            continue

        if board[x][y] != " ":
            print("Эта клетка уже занята")
            continue

        return x, y


def check_win():
    """Функция проверки выигрыша одной из сторон"""
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for each in win_cord:
        symbols = []
        for c in each:
            symbols.append(board[c[0]][c[1]])
            # проверяем выполнение условия выигрыша в списке symbols
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


def tic_tac_toe():
    """Основная функция самой игры"""
    count = 0
    while True:
        game_board()
        count += 1  # вводим счетчик ходов

        if count % 2 == 1:  # первым начинает Х и ходит в нечетные ходы
            print("Ход X")
            x, y = take_coordinates()  # берем координаты для Х
            board[x][y] = "X"  # ставим Х в поле с указанными координатами и добавляем их в board
        else:
            print("Ход 0")  # вторым ходит 0 и ходит каждый четный ход
            x, y = take_coordinates()  # берем координаты для 0
            board[x][y] = "0"  # ставим 0 в поле с указанными координатами и добавляем их в board

        if check_win():  # при выигрыше одной из сторон игра заканчивается
            break

        if count == 9:  # в случае окончания ходов, поле полностью заполнено и игра заканчивается
            print("Ничья")
            break


tic_tac_toe()

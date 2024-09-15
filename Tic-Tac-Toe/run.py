board = [[" " for scr in range(3)] for scr in range(3)]

def game(board):
    round = 0
    win = False
    while win == False:
        print_board(board)
        if round % 2 == 0:
            input_cord("X")
            round += 1
        else:
            input_cord("O")
            round += 1
        if round > 4:
            tmp = check_win(board)
            if tmp:
                print(f"{tmp} выйграл!")
                win = True
                break
        if round == 9:
            print("Ничья!")
            break
    print_board(board)


def check_win(board):
    win_coord = [
        [board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]], [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]], [board[2][0], board[1][1], board[0][2]]
    ]
    for each in win_coord:
        if each == ["X", "X", "X"]:
            return "X"
        if each == ["O", "O", "O"]:
            return "O"
    return False


def input_cord(player_token):
    valid = False
    while valid == False:
        cord_anwser = int(input(f"Куда поставим {player_token}?: "))
        if cord_anwser >= 1 and cord_anwser <= 9:
            row = (cord_anwser - 1) // 3
            col = (cord_anwser - 1) % 3
            if board[row][col] == " ":
                board[row][col] = player_token
                valid = True
            else:
                print("Данная клетка уже занята.")
        else:
            print("Введите номер клетки от 1 до 9. \nКоординаты:  \n|1|2|3| \n|4|5|6| \n|7|8|9|")


def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

game(board)

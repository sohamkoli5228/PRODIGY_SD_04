# ===========================================
# Sudoku Solver
# Developed for Prodigy InfoTech Task-04
# ===========================================

import os

SIZE = 9


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_board(board):

    print()

    for i in range(SIZE):

        if i % 3 == 0 and i != 0:
            print("-" * 25)

        for j in range(SIZE):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if board[i][j] == 0:
                print(".", end=" ")

            else:
                print(board[i][j], end=" ")

        print()

    print()


def find_empty(board):

    for row in range(SIZE):

        for col in range(SIZE):

            if board[row][col] == 0:
                return row, col

    return None


def valid(board, num, pos):

    row, col = pos

    # Row Check
    for i in range(SIZE):

        if board[row][i] == num and col != i:
            return False

    # Column Check
    for i in range(SIZE):

        if board[i][col] == num and row != i:
            return False

    # Box Check
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):

        for j in range(box_x * 3, box_x * 3 + 3):

            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):

    find = find_empty(board)

    if not find:
        return True

    row, col = find

    for number in range(1, 10):

        if valid(board, number, (row, col)):

            board[row][col] = number

            if solve(board):
                return True

            board[row][col] = 0

    return False


def load_sample():

    return [

        [5,3,0,0,7,0,0,0,0],

        [6,0,0,1,9,5,0,0,0],

        [0,9,8,0,0,0,0,6,0],

        [8,0,0,0,6,0,0,0,3],

        [4,0,0,8,0,3,0,0,1],

        [7,0,0,0,2,0,0,0,6],

        [0,6,0,0,0,0,2,8,0],

        [0,0,0,4,1,9,0,0,5],

        [0,0,0,0,8,0,0,7,9]

    ]
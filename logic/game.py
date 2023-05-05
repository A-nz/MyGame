import random
import sys


class Point:

    def __init__(self, r, c):
        self.r = int(r)
        self.c = int(c)


class Game:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.board = self.create_matrix(x, y)

        self.score = 0


    @property
    def board_size(self):
        return self.x

    def board(self):
        return self.board

    def create_matrix(self, x: int, y: int) -> list:
        matrix = []
        for i in range(x):
            matrix.append([])
            for _ in range(y):
                matrix[-1].append(random.randint(1, 4))

        return matrix


class GameService:

    @staticmethod
    def make_move(board, x: int, y: int):
        score = 0
        if GameService.is_cell_has_neighbour(board, x, y):
            score = GameService.find_equal(board, x, y)
            GameService.fill_empty_cells(board)
        return score

    @staticmethod
    def find_equal(board, x: int, y: int):
        score = 0
        cell = board[y][x]
        if (y + 1) < len(board):
            if cell == board[y + 1][x]:
                board[y][x] = 0
                GameService.find_equal(board, x, y + 1)
        if (x + 1) < len(board[0]):
            if cell == board[y][x + 1]:
                board[y][x] = 0
                GameService.find_equal(board, x + 1, y)
        if (y - 1) >= 0:
            if cell == board[y - 1][x]:
                board[y][x] = 0
                GameService.find_equal(board, x, y - 1)
        if (x - 1) >= 0:
            if cell == board[y][x - 1]:
                board[y][x] = 0
                GameService.find_equal(board, x - 1, y)

        board[y][x] = 0
        score += 10

        return score

    @staticmethod
    def fill_empty_cells(board):
        for x in range(len(board[0])):
            temp_list = list()
            for y in range(len(board)):
                if board[y][x] != 0:
                    temp_list.append(board[y][x])
            for y in range(len(board) - len(temp_list)):
                board[y][x] = random.randint(1, 5)
            i = 0
            for y in range(len(board) - len(temp_list), len(board)):
                board[y][x] = temp_list[i]
                i += 1

    @staticmethod
    def is_cell_has_neighbour(board, x: int, y: int) -> bool:
        cell = board[y][x]
        print(cell)

        if (y + 1) < len(board):
            if cell == board[y + 1][x]:
                return True
        if (x + 1) < len(board[0]):
            if cell == board[y][x + 1]:
                return True
        if (y - 1) >= 0:
            if cell == board[y - 1][x]:
                return True
        if (x - 1) >= 0:
            if cell == board[y][x - 1]:
                return True
        return False

    @staticmethod
    def is_game_over(board) -> bool:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if GameService.is_cell_has_neighbour(board, x, y):
                    return False
        return True

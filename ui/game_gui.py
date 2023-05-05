from logic.game import *

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic

white_color = 'background-color:white; border-radius:5px'
red_color = 'background-color:red; border-radius:5px'
yellow_color = 'background-color:yellow; border-radius:5px'
blue_color = 'background-color:blue; border-radius:5px'
green_color = 'background-color:green; border-radius:5px'


class MainWindowUI(QMainWindow):

    def __init__(self):
        super(MainWindowUI, self).__init__()

        uic.loadUi('ui/game_ui.ui', self)
        self.grid = self.findChild(QGridLayout, "fieldLayout")
        self.game = Game(9, 9)
        self.score = self.findChild(QLabel, "scoreField")
        self.board = self.game.board
        self.draw_game_field(self.grid, self.game)

        self.show()

    def draw_game_field(self, layout: QtWidgets.QGridLayout, game: Game):
        point_to_label = dict()
        size = game.board_size
        for row in range(size):
            for column in range(size):
                label = QtWidgets.QLabel()
                label.setAlignment(Qt.AlignCenter)
                cell_value = game.board[row][column]
                point_to_label[(row, column)] = label

                self.assign_color(label, cell_value)
                label.mousePressEvent = self.click_to_move(row, column)
                layout.addWidget(label, row, column)
        self.score.setText(str(self.game.score))
        return point_to_label

    def assign_color(self, label: QLabel, cell_value):
        if cell_value == 1:
            label.setStyleSheet(red_color)
        if cell_value == 2:
            label.setStyleSheet(blue_color)
        if cell_value == 3:
            label.setStyleSheet(green_color)
        if cell_value == 4:
            label.setStyleSheet(yellow_color)

    def click_to_move(self, row, col):
        def click(event):
            self.curr = Point(row, col)
            self.game.score += GameService.make_move(self.board, col, row)
            self.draw_game_field(self.grid, self.game)

        return click

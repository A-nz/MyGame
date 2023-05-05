import sys

from PyQt5.QtWidgets import QApplication

from ui.game_gui import MainWindowUI


def main():
    app = QApplication(sys.argv)
    win = MainWindowUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

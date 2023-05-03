from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QIcon
from main_window import MainWindow
from variables import WINDOW_ICON
from main_display import Display
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON))

    # Criando Display
    display = Display()
    window.addToVLayout(display)

    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()
    


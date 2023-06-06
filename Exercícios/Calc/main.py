from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from main_window import MainWindow
from variables import WINDOW_ICON
from main_display import Display
from buttons import buttonsGrid
from info import Info
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON))

    # Info
    informer = Info('10 * 5 = 50')
    window.addWidgetToVLayout(informer)

    # Criando Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    grid = buttonsGrid(display, informer, window)
    window.vLayout.addLayout(grid)

    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    window.adjustFixedSize()
    window.show()
    app.exec()
    


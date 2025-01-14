import typing
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QApplication, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora de WeS')


    def adjustFixedSize(self):
            self.adjustSize()
            self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
         return QMessageBox(self)

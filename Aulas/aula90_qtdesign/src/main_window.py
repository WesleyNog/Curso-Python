import sys
from typing import Optional

import PySide6.QtCore

from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QObject, QEvent


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.lineEdit.setPlaceholderText('Digite seu nome!')
        self.buttonSend.clicked.connect(self.sendTextToResult)
        self.lineEdit.returnPressed.connect(self.sendTextToResult)
        self.lineEdit.installEventFilter(self)

    def sendTextToResult(self):
        text = self.lineEdit.text()

        if len(self.lineEdit.text()) != 0:
            self.labelResult.setText(text)
        else:
            self.labelResult.setText('Digite seu nome!')

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            text = self.lineEdit.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
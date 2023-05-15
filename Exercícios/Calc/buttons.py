import typing
from PyQt6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE
from main_display import Display
from utils import isEmpty, isNumOrDot

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setItalic(True)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class buttonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀️', 'ˆ', '➗'],
            ['7', '8', '9', '✖️'],
            ['4', '5', '6', '➖'],
            ['1', '2', '3', '➕'],
            ['', '0', '.', '🟰'],
        ]

        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot and not isEmpty:
                    button.setProperty('cssClas', 'specialButton')

                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)


    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
    
    def _insertTextToDisplay(self, button: Button):
        button_text = button.text()
        self.display.insert(button_text)

from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValid

if TYPE_CHECKING:
    from main_display import Display
    from info import Info

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
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀️', 'ˆ', '➗'],
            ['7', '8', '9', '✖️'],
            ['4', '5', '6', '➖'],
            ['1', '2', '3', '➕'],
            ['', '0', '.', '🟰'],
        ]

        self.display = display
        self.info = info
        self._equation = ''


        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClas', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertTextToDisplay, button)
                self._connectClicked(button, slot)
                
            
    def _connectClicked(self, button: Button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: Button):
        text = button.text()
        
        if text == 'C':
            self._connectClicked(button, self._clear)

    def _makeSlot(self, func, *args, **kwargs):
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
    
    def _insertTextToDisplay(self, button: Button):
        button_text = button.text()
        newDisplay = self.display.text() + button_text

        if not isValid(newDisplay):
            return 

        self.display.insert(button_text)


    def _clear(self):
        print('Deu certo')
        self.display.clear()
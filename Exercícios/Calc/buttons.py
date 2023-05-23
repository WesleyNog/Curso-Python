from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValid
import math

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
            ['C', '◀️', 'ˆ', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self._equation = ''
        self._equationInitialValue = 'Sua Conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation  = self._equationInitialValue
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
        
        if text in '+-/*ˆ':
            self._connectClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )
        
        if text in '=':
            self._connectClicked(button, self. _eq)

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
        self._left = None
        self._right = None
        self._op = None
        self.equation  = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValid(displayText) and self._left is None:
            return
        
        if self._left is None:
            self._left = float(displayText)
            
        self._op = buttonText
        self.equation = f'{self._left:.2f} {self._op} ??'


    def _eq(self):
        displayText = self.display.text()

        if not isValid(displayText):
            return

        self._right = float(displayText)
        self.equation = f'{self._left:.2f} {self._op} {self._right:.2f}'
        result = 'error'
        
        try:
            if 'ˆ' in self._equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = round(eval(self.equation), 2)
        except ZeroDivisionError:
            result
        except OverflowError:
            result

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

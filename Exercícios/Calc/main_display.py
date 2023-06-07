from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN
from utils import isEmpty, isNumOrDot

class Display(QLineEdit):
    eqTrigger = Signal()
    delTrigger = Signal()
    clearTrigger = Signal()
    inputTrigger = Signal(str)
    operatorTrigger = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        if key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]:
            self.eqTrigger.emit()
            return event.ignore()

        if key in [KEYS.Key_Backspace, KEYS.Key_Delete]:
            self.delTrigger.emit()
            return event.ignore()
        
        if key in [KEYS.Key_Escape, KEYS.Key_C]:
            self.clearTrigger.emit()
            return event.ignore()

        if key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash,
            KEYS.Key_Asterisk, KEYS.Key_P,
            ]:
            if text.lower() == 'p':
                text = '^'
            self.operatorTrigger.emit(text)
            return event.ignore()
        

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            self.inputTrigger.emit(text)
            return event.ignore()
import sys
from pathlib import Path
from time import sleep
from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, QLabel,
                             QCheckBox, QLineEdit, QSystemTrayIcon
                             )
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QThread
from PyQt6.QtGui import QIcon, QMovie, QPixmap
from datetime import datetime

#from random import choice
import secrets

random = secrets.SystemRandom()
ALL_RESULTS = 'Resultados.txt'
current_date = datetime.now()
format_date = current_date.strftime('%d/%b/%y (%H:%M)')
numbers = list(range(1, 61))
# count = 0

# quantidade = int(input('Quantos Resultados? '))


class AppMegaSena:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = QWidget()


    def window_create(self):
        self.window.setWindowTitle('Mega-Sena')
        self.window.setFixedSize(350, 130)
        self.window.setWindowIcon(QIcon('megasena-icon.png'))
        self.logo_system = QSystemTrayIcon(QIcon('megasena-icon.png'), parent=None)
        self.logo_system.setToolTip('MegaSena')
        # self.window.setStyleSheet(
        #     '''background-color: white;
        #     '''
        # )
        # self.window.setWindowIcon(QIcon('logo.png'))

        self.label_image = QLabel(self.window)
        self.label_image.setFixedSize(350, 130)
        pixmap = QPixmap('mega_sena_resized.png')
        self.label_image.setPixmap(pixmap)

        self.animation_window = QLabel(self.window)
        self.animation_win_gif = QMovie('confetti-4-unscreen.gif')
        self.animation_window.setMovie(self.animation_win_gif)
        self.animation_win_gif.start()
        self.animation_window.setFixedSize(350, 130)
        self.animation_window.setVisible(False)


        self.button = QPushButton('🍀', self.window)
        self.button.setGeometry(145, 80, 70, 30)
        self.button.clicked.connect(self.sortear)


        self.label = QLabel('Boa', self.window)
        self.label.setGeometry(65, 1, 150, 30)
        self.label.setStyleSheet(
            '''font-size: 25px;
            color: #064369
            '''
            )

        ## Creat label's for sorted numbers display ##

        self.number_01 = QLabel('S', self.window)
        self.number_01.setGeometry(60, 30, 35, 35)
        self.number_01.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_01.setStyleSheet(
            '''border-radius: 17px;
            font-size: 20px;
            font-family: Broadway;
            color: #064369;
            border: 1px solid white;
            background-color: #4FB549;
            '''
            )
        
        
        self.number_02 = QLabel('O', self.window)
        self.number_02.setGeometry(100, 30, 35, 35)
        self.number_02.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_02.setStyleSheet(
            '''border-radius: 17px;
            font-size: 20px;
            font-family: Broadway;
            color: #064369;
            border: 1px solid white;
            background-color: #4FB549;
            '''
            )


        self.number_03 = QLabel('R', self.window)
        self.number_03.setGeometry(140, 30, 35, 35)
        self.number_03.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_03.setStyleSheet(
            '''border-radius: 17px;
            font-size: 20px;
            font-family: Broadway;
            color: #064369;
            border: 1px solid white;
            background-color: #4FB549;
            '''
            )
        

        self.number_04 = QLabel('T', self.window)
        self.number_04.setGeometry(180, 30, 35, 35)
        self.number_04.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_04.setStyleSheet(
            '''border-radius: 17px;
            font-size: 20px;
            font-family: Broadway;
            color: #064369;
            border: 1px solid white;
            background-color: #4FB549;
            '''
            )


        self.number_05 = QLabel('E', self.window)
        self.number_05.setGeometry(220, 30, 35, 35)
        self.number_05.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_05.setStyleSheet(
            '''border-radius: 17px;
            font-size: 20px;
            font-family: Broadway;
            color: #064369;
            border: 1px solid white;
            background-color: #4FB549;
            '''
            )
        

        self.number_06 = QLabel('!', self.window)
        self.number_06.setGeometry(260, 30, 35, 35)
        self.number_06.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_06.setStyleSheet(
            '''border-radius: 17px;
            font-size: 20px;
            font-family: Broadway;
            color: #064369;
            border: 1px solid white;
            background-color: #4FB549;
            '''
            )
        
        self.default = QCheckBox('Config', self.window)
        self.default.move(10, 110)
        self.default.setStyleSheet(
            '''font-size: 10px;
            color: #064369;
            '''
        )
        self.default.stateChanged.connect(self.view_config)

        self.save_file = QCheckBox('Salvar Resultado?', self.window)
        self.save_file.move(20, 110)
        self.save_file.setVisible(False)
        self.save_file.setStyleSheet(
            '''font-size: 10px;
            color: #064369;
            '''
        )


        # Criar a animação
        self.animation_up = QPropertyAnimation(self.default, b"geometry")
        self.animation_up.setDuration(600) # duração em milissegundos
        self.animation_up.setStartValue(QRect(10, 95, 100, 50)) # posição inicial do botão
        self.animation_up.setEndValue(QRect(10, 50, 100, 50)) # posição final do botão

        self.animation_down = QPropertyAnimation(self.default, b"geometry")
        self.animation_down.setDuration(600) # duração em milissegundos
        self.animation_down.setStartValue(QRect(10, 50, 100, 50)) # posição inicial do botão
        self.animation_down.setEndValue(QRect(10, 95, 100, 50)) # posição final do botão

        self.num_start_name = QLabel('DE:', self.window)
        self.num_start_name.move(21, 88)
        self.num_start_name.setVisible(False)
        self.num_start_name.setStyleSheet(
            '''font-size: 10px;
            color: #064369;
            '''
        )
        self.num_start = QLineEdit('1', self.window)
        self.num_start.setGeometry(40, 88, 22, 14)
        self.num_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.num_start.setMaxLength(2)
        self.num_start.setVisible(False)
        self.num_start.setStyleSheet(
            '''border-radius: 7px;
            '''
        )  

        self.num_end_name = QLabel('ATÉ:', self.window)
        self.num_end_name.move(66, 88)
        self.num_end_name.setVisible(False)
        self.num_end_name.setStyleSheet(
            '''font-size: 10px;
            color: #064369;
            '''
        )
        self.num_end = QLineEdit('60', self.window)
        self.num_end.setGeometry(87, 88, 22, 14)
        self.num_end.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.num_end.setMaxLength(2)
        self.num_end.setVisible(False)
        self.num_end.setStyleSheet(
            '''border-radius: 7px;
            '''
        )
    
        self.window.show()
        self.app.exec()
        self.window.close()


    def view_config(self):
        if self.default.isChecked():
            self.animation_up.start()
            # sleep(5)
            self.save_file.setVisible(True)
            self.num_start.setVisible(True)
            self.num_start_name.setVisible(True)
            self.num_end.setVisible(True)
            self.num_end_name.setVisible(True)
        else:
            self.animation_down.start()
            self.save_file.setVisible(False)
            self.num_start.setVisible(False)
            self.num_start_name.setVisible(False)
            self.num_end.setVisible(False)
            self.num_end_name.setVisible(False)
            


    def sortear(self):
        ## Condição para escolher faixa diferente de números ##
        value_start = self.num_start.text()
        value_end = self.num_end.text()
        start = int(value_start)
        end = int(value_end)
        another_number = list(range(start, (end + 1)))

        # while count != quantidade:
        result = []
        while len(result) != 6:
            if not self.default.isChecked():
                for n in numbers:
                    n = random.choice(numbers)
                    if n not in result:
                        result.append(n)
                    break
            else:
                if end > start:
                    for n in another_number:
                        n = random.choice(another_number)
                        if n not in result:
                            result.append(n)
                        break
                
        order_results = sorted(result)
        if self.save_file.isChecked():
            with open(ALL_RESULTS, 'a') as arquivo:
                arquivo.write(f'{format_date}: {order_results}')
                arquivo.write('\n')

        # concatenado = int(''.join(map(str, order_results)))
        # count += 1
        
        self.number_01.setText(str(order_results[0]))
        self.number_02.setText(str(order_results[1]))
        self.number_03.setText(str(order_results[2]))
        self.number_04.setText(str(order_results[3]))
        self.number_05.setText(str(order_results[4]))
        self.number_06.setText(str(order_results[5]))

        self.label.setText('Jogue:')
        self.animation_window.setVisible(True)


class MyThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)

    def whait(self):
        AppMegaSena.view_config()

if __name__ == '__main__':
    app = AppMegaSena()
    app.window_create()
    thread = MyThread()
    
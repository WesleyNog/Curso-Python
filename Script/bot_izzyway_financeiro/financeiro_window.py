import sys
import os
import platform
import pandas as pd
from datetime import datetime
from pathlib import Path
from threading import Thread
from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, QLabel, 
                             QLineEdit, QFileDialog, QProgressBar, QCheckBox, 
                             QSystemTrayIcon
                             )
from PyQt6.QtGui import QIcon, QPixmap, QMovie
from PyQt6.QtCore import QSize, Qt, QTimer
import class_robot

URL = 'https://app.izzyway.com.br/Account/Login#'

BOT = class_robot.RoboIzzyWay()
BOT.driver.get(URL)
DATA = datetime.now()
DATA_FORMAT = DATA.strftime('%d_%m_%Y')



class AppFinanceiroBriejer:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = QWidget()

        self.VALID_MAIL = ['@', '.com']
        self.ARQUIVO = None
        self.DATA_FORMAT = DATA.strftime('%d_%m_%Y')
        self.CONT = 0
        self.FAIL = 0

    def window_create(self, func=None):
        self.window.setWindowTitle('Briejer - Lançamentos [CONTAS A PAGAR]')
        self.window.setFixedSize(650, 380)
        self.window.setWindowIcon(QIcon('IconBriejer_EDIT_02.png'))
        icon_system = QSystemTrayIcon(QIcon('IconBriejer_EDIT_02.png'), parent=None)
        icon_system.setToolTip('Briejer')
        # self.window.setStyleSheet(
        #     "background-color: #00F4C8;"
        # )
        

        ## Elementos informar o LOGIN do USUARIO ##
        self.login_name = QLabel('LOGIN', self.window)
        self.login_name.move(231, 9)
        self.send_login = QLineEdit(self.window)
        self.send_login.returnPressed.connect(self.set_login)
        self.send_login.setGeometry(230, 25, 190, 20)
        self.send_login.setStyleSheet(
            '''border-radius: 3px;
            '''
        )

        ## Elementos informar a SENHA do USUARIO ##
        self.password_name = QLabel('SENHA', self.window)
        self.password_name.move(231, 50)
        self.send_password = QLineEdit(self.window)
        self.send_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.send_password.returnPressed.connect(self.set_login)
        self.send_password.setGeometry(230, 65, 190, 20)
        self.send_password.setStyleSheet(
            '''border-radius: 3px;
            '''
        )

        ## Este e a LOGOMARCA em cima do Label principal ##
        self.label_icon_logo = QLabel(self.window)
        self.pixmap_logo = QPixmap('logo_briejer-remov.png')
        self.label_icon_logo.setPixmap(self.pixmap_logo)
        self.label_icon_logo.resize(221, 85)
        self.label_icon_logo.move(10, 9)

        ## Icon USERS em cima do Label principal ##
        self.label_icon_user = QLabel(self.window)
        self.pixmap_user = QPixmap('user-re_resized.png')
        self.label_icon_user.setPixmap(self.pixmap_user)
        self.label_icon_user.resize(85, 85)
        self.label_icon_user.move(556, 0)
        self.label_icon_user.setVisible(False)
        self.label_user = QLabel(self.window)
        self.label_user.setGeometry(556, 76, 70, 15)
        self.label_user.setText('--')
        self.label_user.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_user.setVisible(False)
        self.label_user.setStyleSheet(
            '''font-size: 12px;
            font: bold Cursive;
            border-radius: 7px;
            border: 1px solid black;
            background-color: white;
            '''
        )
        
        ## Icone animado de LOGIN ##
        self.animation_login = QLabel(self.window)
        self.animation_login_gif = QMovie('profile-small.gif')
        self.animation_login.setMovie(self.animation_login_gif)
        self.animation_login_gif.start()
        self.animation_login.setGeometry(530, 20, 70, 70)
        self.animation_login.setVisible(False)

        self.err = 30

        ## Label com nome de LANÇAMENTO ##
        self.label_name_sucess = QLabel('LANCAMENTOS', self.window)
        self.label_name_sucess.resize(143, 30)
        self.label_name_sucess.move(9, 100)
        self.label_name_sucess.setStyleSheet(
            '''border :1px solid silver;
            border-radius: 7px;
            background-color: #E5EFEF'''
        )

        ## Indicativo do TOTAL de LANÇAMENTO ##
        self.label_total_sucess = QLabel('TOTAL: --', self.window)
        self.label_total_sucess.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_total_sucess.resize(75, 30)
        self.label_total_sucess.move(154, 100)
        self.label_total_sucess.setStyleSheet(
            '''border :1px solid #3D1F2A;
            border-radius: 7px;
            background-color: white'''
        )

        ## Indicativo do TOTAL de LANÇAMENTO ##
        self.label_remaining_sucess = QLabel(f'RESTANTE: --', self.window)
        self.label_remaining_sucess.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_remaining_sucess.resize(90, 30)
        self.label_remaining_sucess.move(230, 100)
        self.label_remaining_sucess.setStyleSheet(
            '''border :1px solid #3D1F2A;
            border-radius: 7px;
            background-color: white'''
        )

        ## Este e um Label para mostrar os LANÇAMENTOS
        self.label_log_sucess = QLabel(self.window)
        self.label_log_sucess.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label_log_sucess.setStyleSheet(
            '''border :1px solid silver;
            border-radius: 7px;
            background-color: #E5EFEF'''
        )
        self.label_log_sucess.resize(312, 150)
        self.label_log_sucess.move(9, 133)

        ## Indicatico da Label de ERROR ##
        self.label_name_error = QLabel('ERROR', self.window)
        self.label_name_error.resize(218, 30)
        self.label_name_error.move(325, 100)
        self.label_name_error.setStyleSheet(
            '''border :1px solid silver;
            border-radius: 7px;
            background-color: #E5EFEF'''
        )

        ## Indicativo da Label de LANÇAMENTO ##
        self.label_number_error = QLabel('ERRO: --', self.window)
        self.label_number_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_number_error.resize(90, 30)
        self.label_number_error.move(545, 100)
        self.label_number_error.setStyleSheet(
            '''border :1px solid #3D1F2A;
            border-radius: 7px;
            background-color: white'''
        )
        
        ## Este e um Label para mostrar os ERROS ##
        self.label_log_error = QLabel(self.window)
        self.label_log_error.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_log_error.setStyleSheet(
            '''border :1px solid silver;
            border-radius: 7px;
            background-color: #E5EFEF'''
        )
        self.label_log_error.resize(312, 150)
        self.label_log_error.move(325, 133)

        ## Botão para procurar um arquivo Excel ##
        self.button_seach = QPushButton(self.window)
        self.button_seach.setEnabled(False)
        self.button_seach.setGeometry(570, 290, 70, 30)
        self.button_seach.clicked.connect(self.choose_file)
        self.button_seach.setIcon(QIcon('excel.png'))
        self.button_seach.setIconSize(QSize(60, 20))
        self.button_seach.setStyleSheet(
            '''
            QPushButton {
                border-radius: 7px;
                background-color: white;
                color: black;
                font-size: 13px;
                padding: 3px;
            }
            QPushButton:hover {
                background-color: #C4DDC5;
            }
            '''
        )
        
        ## Botão para começar a roda o códiigo ##
        self.button_go = QPushButton('Start!', self.window)
        self.button_go.setEnabled(False)
        self.button_go.setGeometry(290, 323, 70, 50)
        self.button_go.setStyleSheet(
            '''
            QPushButton {
                border-radius: 7px;
                background-color: #F08835;
                color: white;
                font-size: 13px;
                padding: 3px;
            }
            QPushButton:hover {
                background-color: #f8d573;
                color: black;
            }
            '''
        )
        self.button_go.clicked.connect(self.start)

        ## Label apra mostrar o criador do APP ##
        self.label_copyright = QLabel('© WesTecnology', self.window)
        self.label_copyright.move(10, 367)
        self.label_copyright.setStyleSheet('font-size: 08px')

        self.label_version = QLabel('V1.0.0', self.window)
        self.label_version.move(610, 367)
        self.label_version.setStyleSheet('font-size: 08px')

        ## Barra de caminho para escolha do arquivo ##
        self.excel_path = QLineEdit(self.window)
        self.excel_path.setReadOnly(True)
        self.excel_path.setGeometry(10, 290, 550, 30)
        self.excel_path.setStyleSheet(
            '''border-radius: 7px;
            border: 1px solid silver;
            '''
        )


        ## Este e uma caixa de checagem para adicionar ou não um e-mail à ser enviado ##
        self.check_box_save = QCheckBox('Enviar por e-mail?', self.window)
        self.check_box_save.setEnabled(False)
        self.send_mail = QLineEdit('@briejer.com.br', self.window)
        self.send_mail.returnPressed.connect(self.start)
        self.send_mail.setVisible(False)
        self.send_mail.setStyleSheet(
            '''border-radius: 10px;
            border: 1px solid silver;
            '''
        )
        self.check_box_save.setGeometry(10, 315, 128, 30)
        self.check_box_save.stateChanged.connect(self.set_email_check)

        ## Mensagem de e-mail enviado com sucesso ##
        self.mail_sucess = QLabel('Enviado c/ Sucesso!', self.window)
        self.mail_sucess.move(157, 324)
        self.mail_sucess.setStyleSheet(
            '''font-size: 10px;
            color: #1BD622;
            '''
        )
        self.mail_sucess.setVisible(False)

        self.progress_bar = QProgressBar(self.window)
        self.progress_bar.setGeometry(230, 88, 195, 10)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        
        self.window.show()
        self.app.exec()
        self.window.close()


    def set_login(self):
        self.animation_login.setVisible(True)
        if len(self.send_login.text()) and len(self.send_password.text()) != 0:
            if self.VALID_MAIL[0] in self.send_login.text() and \
            self.VALID_MAIL[1] in self.send_login.text().lower() and \
            len(self.send_login.text()) >= 8 and self.send_login.text().find(self.VALID_MAIL[0]) > 0 and \
            self.send_login.text().lower().find(self.VALID_MAIL[1]) > 0:
                BOT.logar_user(self.send_login.text(), self.send_password.text())
                if BOT.GET_NAME_USER != None:
                    self.animation_login.setVisible(False)
                    self.label_user.setText(BOT.GET_NAME_USER)
                    self.label_icon_user.setVisible(True)
                    self.label_user.setVisible(True)
                    self.button_seach.setEnabled(True)
                    self.button_go.setEnabled(True)
                    self.check_box_save.setEnabled(True)
                    self.send_login.setEnabled(False)
                    self.send_password.setEnabled(False)
                    self.send_mail.setText(self.send_login.text().lower())
                    self.label_log_error.setText('')
                else:
                    self.label_log_error.setText(f'LOGIN e/ou SENHA estão INVÁLIDOS!')
                    self.animation_login.setVisible(False)
            else:
                self.label_log_error.setText('LOGIN fora do PADRÃO')
        else:
            self.label_log_error.setText('LOGIN e SENHA são OBRIGATÓRIOS')


    def choose_file(self):
        file_name = QFileDialog.getOpenFileName(None, 'Procurar Planilha', '', '*.xlsx *.xls')
        path_file = file_name[0]
        self.excel_path.setText(path_file)
        if len(self.excel_path.text()) != 0:
            if platform.system() == 'Windows':
                path_file = path_file.replace('/', '\\')
            self.ARQUIVO = path_file
            BOT.LER = pd.read_excel(self.ARQUIVO)
            BOT.QNT_LANCAMENTO = len(BOT.LER)
            self.label_total_sucess.setText(f'TOTAL: {BOT.QNT_LANCAMENTO}')
            self.label_remaining_sucess.setText(f'RESTANTE: {BOT.QNT_LANCAMENTO - self.CONT}')
        else:
            self.label_total_sucess.setText('TOTAL: --')
            self.label_remaining_sucess.setText('RESTANTE: --')

    ## Método para dar início ao código (BOT) ##
    def start(self, funcao=None):
        if not self.check_box_save.isChecked():
            if len(self.excel_path.text()) != 0:
                BOT.LOG = self.ARQUIVO.replace('.xlsx', 'txt') # 'LOG_' + BOT.GET_NAME_USER + '_' + self.DATA_FORMAT + self.ARQUIVO.replace('.xlsx', 'txt')
                self.button_seach.setEnabled(False)
                self.button_go.setEnabled(False)
                self.check_box_save.setEnabled(False)
                self.label_log_sucess.setText(self.excel_path.text())
                self.progress_bar.setVisible(True)
                self.label_log_error.setText('')
                self.timer.start(BOT.QNT_LANCAMENTO)
            else:
                self.label_log_error.setText('ABRA UM ARQUIVO EXCEL VÁLIDO!')
        else:
            if self.VALID_MAIL[0] in self.send_mail.text() and \
            self.VALID_MAIL[1] in self.send_mail.text() and \
            len(self.send_mail.text()) != 0:
                if len(self.excel_path.text()) != 0:
                    BOT.LOG = self.ARQUIVO.replace('.xlsx', 'txt') # 'LOG_' + BOT.GET_NAME_USER + '_' + self.DATA_FORMAT + self.ARQUIVO.replace('.xlsx', 'txt')
                    self.button_seach.setEnabled(False)
                    self.button_go.setEnabled(False)
                    self.check_box_save.setEnabled(False)
                    self.send_mail.setEnabled(False)
                    self.label_log_sucess.setText(self.excel_path.text())
                    self.progress_bar.setVisible(True)
                    self.label_log_error.setText('')
                    self.timer.start(BOT.QNT_LANCAMENTO)
                else:
                    self.label_log_error.setText('ABRA UM ARQUIVO EXCEL VÁLIDO!')
            else:
                self.label_log_error.setText('E-mail inválido')


    ## Método para adicionar uma barra de progresso na TELA ##
    def update_progress(self):
        value = self.progress_bar.value()
        if value < BOT.QNT_LANCAMENTO:
            self.progress_bar.setValue(self.CONT)
        else:
            self.timer.stop()


    def set_email_check(self):
        if self.check_box_save.isChecked():
            self.send_mail.setVisible(True)
            self.send_mail.setGeometry(10, 340, 250, 20)
        else:
            self.send_mail.setVisible(False)


    def set_text_label(self, text: str, stats='sucesso'):
        set_text = text
        if stats.lower() == 'sucesso':
            self.label_log_sucess.setText(f'Seja bem vindo {set_text}!')
        else:
            self.label_log_error.setText(set_text)


class MethodThread(Thread):
    def __init__(self):
        super().__init__()

    def login(self):
        AppFinanceiroBriejer.set_login()



if __name__ == '__main__':
    app = AppFinanceiroBriejer()
    app.window_create()
    # thread_login = Thread(MethodThread)

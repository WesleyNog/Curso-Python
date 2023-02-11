import os
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from string import Template

load_dotenv()

# Caminho arquivo HTML
CAMINHO_ARQUIVO = Path(__file__).parent / 'aula78.html'

# Dados do remetente e destinatário
remetente = os.getenv('USER_MAIL', '')
destinatario = 'wesmark85@gmail.com'

# Configurações SMTP
smtp_server = os.getenv('SMTP_SEVER', '')
smtp_port = os.getenv('SMTP_PORT', '')
smtp_username = os.getenv('USER_MAIL', '')
smtp_passoword = os.getenv('USER_PASSOWORD', '')

# Mensagem de Texto
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
   texto_arquivo = arquivo.read()
   template = Template(texto_arquivo)
   texto_email = template.substitute(nome='Helloá')

# Transformar nossa mensagem em MIMEMultpart
mine_multpart = MIMEMultipart()
mine_multpart['from'] = remetente
mine_multpart['to'] = destinatario
mine_multpart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mine_multpart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_passoword)
    server.send_message(mine_multpart)
    print('E-mail enviado com sucesso!')

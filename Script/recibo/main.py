import os
import pandas as PD
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from gerar_recibo import criar_recibo

mult = 0
count = 1
current_date = datetime.now().strftime('%d/%m/%Y')
# Inicializar o canvas (a página PDF)
c = canvas.Canvas(os.path.join(os.getcwd(), 'recibo.pdf'), pagesize=A4)

# Lendo o arquivo Excel
excel = PD.read_excel(os.path.join(os.getcwd(), 'FOLHA EXTRA JANEIRO 2024.xlsx'))
df_excel = PD.DataFrame(excel)
qnt_recibo = len(df_excel['VALOR LIQUIDO A RECEBER'])

for indice, linha in df_excel.iterrows():
    if str(linha['PGTO']).upper() == 'DINHEIRO':
        nome = linha['EMPREGADO']
        valor = round(linha['VALOR LIQUIDO A RECEBER'], 2)
        if str(linha['EMPRESA']).upper() == 'EMPORIO':
            empresa = 'Empório de Fátima Confeitaria LTDA'
            cnpj = '11.322.565/0001-01'
            endereco = 'AV DEPUTADO OSVALDO STUDART N 250 - FÁTIMA'
        else:
            empresa = 'Maria Vasconcelos de Souza LTDA'
            cnpj = '51.468.741/0001-32'
            endereco = 'RUA MINISTRO JOAQUIM BASTOS N 380 - FÁTIMA'


        if count != 2:
            criar_recibo(c, nome, f'{valor:.2f}', current_date, empresa, cnpj, endereco, mult)
            mult += 450
            count += 1
        else:
            criar_recibo(c, nome, f'{valor:.2f}', current_date, empresa, cnpj, endereco, mult)
            c.showPage()
            mult = 0
            count = 1

# Salvar o PDF
c.save()
os_name = os.name
if os_name == 'nt':
    os.system(f'start recibo.pdf')  # Windows
else:
    os.system(f'open recibo.pdf')  # Linux/macOS
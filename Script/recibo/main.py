import os
import math
import pandas as PD
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from gerar_recibo import create_receipt, divisor_line

mult = 0
count = 1
current_date = datetime.now().strftime('%d/%m/%Y')
# Inicializar o canvas (a página PDF)
c = Canvas(os.path.join(os.getcwd(), f'recibo - {current_date.replace("/", "")}.pdf'), pagesize=A4)

# Lendo o arquivo Excel
excel = PD.read_excel(os.path.join(os.getcwd(), 'SALARIO - JANEIRO 24.xlsx'))
df_excel = PD.DataFrame(excel)
qnt_receipt = len(df_excel['LIQUIDO A RECEBER'])

for index, line in df_excel.iterrows():
    try:
        if not math.isnan(line['LIQUIDO A RECEBER']):
            name = line['EMPREGADO']
            value = round(line['LIQUIDO A RECEBER'], 2)
            if str(line['EMPRESA']).upper() == 'EMPORIO':
                company = 'Empório de Fátima Confeitaria LTDA'
                cnpj = '11.322.565/0001-01'
                adress = 'AV DEPUTADO OSVALDO STUDART N 250 - FÁTIMA'
            else:
                company = 'Maria Vasconcelos de Souza LTDA'
                cnpj = '51.468.741/0001-32'
                adress = 'RUA MINISTRO JOAQUIM BASTOS N 380 - FÁTIMA'
            data = line['DATA']
            emitido = line['EMITIDO']
            autorizado = line['AUTORIZADO']
            gerente = line['GERENTE']

            if count != 2:
                create_receipt(c, name, value, data, company, cnpj, adress, gerente, emitido, autorizado, mult)
                mult += 450
                count += 1
            else:
                create_receipt(c, name, value, data, company, cnpj, adress, gerente, emitido, autorizado, mult)
                divisor_line(c)
                c.showPage()
                mult = 0
                count = 1
    except TypeError:
        pass

# Salvar o PDF
c.save()
# os_name = os.name
# if os_name == 'nt':
#     os.system(f'start recibo - {current_date.replace("/", "_")}.pdf')  # Windows
# else:
#     os.system(f'open recibo - {current_date.replace("/", "_")}.pdf')  # Linux/macOS

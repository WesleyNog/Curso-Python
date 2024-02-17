import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from gerar_recibo import criar_recibo

mult = 0
count = 1
valor_rec = 100.50
current_date = datetime.now().strftime('%d/%m/%Y')
# Inicializar o canvas (a página PDF)
c = canvas.Canvas('recibo.pdf', pagesize=A4)

for i, num in enumerate(range(0, 7)):
    if count != 2:
        criar_recibo(c, 'Wesley Nogueira P. da Silva', valor_rec, current_date, mult)
        mult += 450
        count += 1
        valor_rec += 112.50
    else:
        criar_recibo(c, 'Wesley Nogueira P. da Silva', valor_rec, current_date, mult)
        c.showPage()
        mult = 0
        count = 1
        valor_rec += 112.50

# Salvar o PDF
c.save()
os_name = os.name
if os_name == 'nt':
    os.system(f'start recibo.pdf')  # Windows
else:
    os.system(f'open recibo.pdf')  # Linux/macOS
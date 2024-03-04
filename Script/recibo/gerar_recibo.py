import os
import math
from datetime import datetime
from num2words import num2words
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas

current_date = datetime.now().strftime('%d/%m/%Y')
c = Canvas(os.path.join(os.getcwd(), 'recibo.pdf'), pagesize=A4)


def create_receipt(
        c: Canvas, nome: str, valor: float | int, data: str, empresa: str, cnpj: str, end: str, gerente: str, 
        emissor: str, autorizacao: str, mult_y: int=0
        ):
    print(f'Data de dentro da função: {data}')

    # Adicionar o título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(45, 800 - mult_y, "RECIBO DE PAGAMENTO")
    c.setFont("Helvetica", 10)
    c.drawString(330, 805 - mult_y, empresa.upper())
    c.drawString(330, 795 - mult_y, cnpj)

    # Adicionar retângulo
    c.rect(25, 480 - mult_y, 545, 350)  # coordenadas x, y, largura, altura | Retângulo Externo 01
    c.rect(27, 482 - mult_y, 541, 346)  # coordenadas x, y, largura, altura | Retângulo Externo 02
    c.rect(35, 790 - mult_y, 525, 30)  # coordenadas x, y, largura, altura | Retângulo Superior
    c.rect(35, 490 - mult_y, 525, 30)  # coordenadas x, y, largura, altura | Retângulo Inferior

    # Corpo do recibo
    c.drawString(75, 770- mult_y, 'Eu, ')
    c.setFont("Helvetica-Bold", 11)
    c.drawString(100, 770 - mult_y, nome.upper())

    # Texto do Corpo
    c.setFont("Helvetica", 10)
    c.drawString(60, 740 - mult_y, f'Declaro que recebi da empresa {empresa.upper()}')
    c.drawString(60, 728 - mult_y, 'A importância de: ')
    c.setFont("Helvetica-Bold", 11)
    c.drawString(145, 728 - mult_y, num2words(valor, lang="pt_BR", to="currency").upper())

    # Valor numeral
    c.setFont("Helvetica-Bold", 18)
    c.drawString(60, 707 - mult_y, f'R$ {str(valor).replace(".", ",")}')

    # Texto Final
    c.setFont("Helvetica", 10)
    c.drawString(60, 610 - mult_y, 'Assino o presente recibo dando quitação dos valores.')
    c.drawString(60, 590 - mult_y, 'Assinatura: ')
    c.line(145, 590 - mult_y, 350, 590 - mult_y)
    c.drawString(420, 590 - mult_y, 'Data: ')
    c.line(450, 590 - mult_y, 550, 590 - mult_y)
    verify_info(c, 470, 592, mult_y, data, current_date)
    c.drawString(60, 575 - mult_y, 'Emitido por: ')
    verify_info(c, 145, 575, mult_y, emissor, 'Tainã da Silva')
    c.drawString(60, 560 - mult_y, 'Autorizado por: ')
    verify_info(c, 145, 560, mult_y, autorizacao, 'Amanda S. Vilar')

    try:
        if not math.isnan(gerente):
            c.drawString(420, 577 - mult_y, 'Gerente: ')
            c.drawString(460, 577 - mult_y, gerente)
    except TypeError:
        pass

    # Rodapé
    c.setFont("Helvetica-Bold", 11)
    c.drawString(155, 507 - mult_y, end.upper())
    c.drawString(170, 493 - mult_y, 'FORTALEZA-CE Telefone - (85) 3444-4019')

def divisor_line(c: Canvas):
    # Linha divisória
    c.setLineWidth(1)  # Define a largura da linha
    c.setDash(2, 2)  # Define o padrão da linha pontilhada
    c.line(25, 435, 570, 435)  # coordenadas x1, y1, x2, y2

def verify_info(c: Canvas, x: int | float, y: int | float, mult: int | float, info: str, hardcode: str):
    try:
        print('info: ', info, math.isnan(info))
        if not math.isnan(info):
            c.drawString(x, y - mult, info)
        else:
            c.drawString(x, y - mult, hardcode)
    except TypeError:
        c.drawString(x, y - mult, hardcode)
        


if __name__ == '__main__':
    # Exemplo de uso
    create_receipt(
        c ,'Wesley Nogueira P. da Silva', 100.50, '17/02/2024', 'WNH Slucions', 
        '99.999.999/0009-99', 'Rua Testando N 999 - Bairro Teste', 'Wesley'
        )
    divisor_line(c)
    c.save()

    os_name = os.name
    if os_name == 'nt':
        os.system(f'start recibo.pdf')  # Windows
    else:
        os.system(f'open recibo.pdf')  # Linux/macOS

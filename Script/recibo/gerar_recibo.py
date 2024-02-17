import os
from num2words import num2words
from datetime import datetime

EMPRESA = 'MARIA VASCONCELOS DE SOUZA LTDA'
CNPJ = '51.468.741/0001-32'
current_date = datetime.now().strftime('%d/%m/%Y')

def criar_recibo(c, nome, valor, data, mult_y=0, emissor='Tainã da Silva', autorizacao='Amanda S. Vilar'):

    # Adicionar o título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(45, 800 - mult_y, "RECIBO DE PAGAMENTO")
    c.setFont("Helvetica", 10)
    c.drawString(330, 805 - mult_y, EMPRESA)
    c.drawString(330, 795 - mult_y, CNPJ)

    # Adicionar retângulo
    c.rect(25, 480 - mult_y, 545, 350)  # coordenadas x, y, largura, altura | Retângulo Externo 01
    c.rect(27, 482 - mult_y, 541, 346)  # coordenadas x, y, largura, altura | Retângulo Externo 01
    c.rect(35, 790 - mult_y, 525, 30)  # coordenadas x, y, largura, altura | Retângulo Superior
    c.rect(35, 490 - mult_y, 525, 30)  # coordenadas x, y, largura, altura | Retângulo Inferior

    # Corpo do recibo
    c.drawString(75, 770- mult_y, 'Eu, ')
    c.setFont("Helvetica-Bold", 11)
    c.drawString(100, 770 - mult_y, nome)

    # Texto do Corpo
    c.setFont("Helvetica", 10)
    c.drawString(60, 740 - mult_y, f'Declaro que recebi da empresa {EMPRESA}')
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
    c.drawString(60, 575 - mult_y, 'Emitido por: ')
    c.drawString(145, 575 - mult_y, emissor)
    c.drawString(60, 560 - mult_y, 'Autorizado por: ')
    c.drawString(145, 560 - mult_y, autorizacao)
    c.drawString(420, 590 - mult_y, 'Data: ')
    c.line(450, 590 - mult_y, 550, 590 - mult_y)
    c.drawString(470, 592 - mult_y, data)

    # Rodapé
    c.setFont("Helvetica-Bold", 11)
    c.drawString(155, 507 - mult_y, 'RUA MINISTRO JOAQUIM BASTOS N 380 - FÁTIMA')
    c.drawString(170, 493 - mult_y, 'FORTALEZA-CE Telefone - (85) 3444-4019')


if __name__ == '__main__':
    # Exemplo de uso
    criar_recibo('Wesley Nogueira P. da Silva', 100.50, current_date)

    os_name = os.name
    if os_name == 'nt':
        os.system(f'start recibo.pdf')  # Windows
    else:
        os.system(f'open recibo.pdf')  # Linux/macOS
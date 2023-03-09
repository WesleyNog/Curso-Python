import class_robot as cb;
import financeiro_window as wd
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from datetime import datetime
from time import sleep

URL = 'https://app.izzyway.com.br/Account/Login#'
EMAIL = '##################'


ROBO = cb.RoboIzzyWay()
ROBO.driver.get(URL)
TELA = wd.AppFinanceiroBriejer()


ROBO.logar_bot()
TELA.set_text_label('Logando...')
sleep(10)
try:
    ROBO.modulos('FINANCEIRO')
except:
    ROBO.driver.refresh()
    print('ERROR: Falha no carregamento!')
    print('Retomando...')
    sleep(10)
    ROBO.modulos('FINANCEIRO')


with open(ROBO.LOG, 'a+') as arquivo:
        arquivo.write('#' * 30)
        arquivo.write('\n')
        arquivo.write(f'{ROBO.QNT_LANCAMENTO} LANÇAMENTOS existentes!\n')
        arquivo.write('Realizando lancamentos!\n')
        arquivo.write('\n')
        arquivo.write('#' * 30)
        arquivo.write('\n')

count = 0

# LOOP
for i, row in ROBO.LER.iterrows():
    ROBO.select_store(row['LOJA'])
    sleep(1)
    ROBO.new_insert()
    if str(row['PAGO']).upper() == 'NÃO':
        try:
            ROBO.fill_in_release(
                    row['PLANO'], row['DOCUMENTO'], row['PARTICIPANTE'], \
                    row['EMISSAO'], row['VENCIMENTO'], row['VALOR'], \
                    row['HISTORICO'], row['FORMA DE PAGAMENTO'], row['DATA DE PAGAMENTO']
            )
        except:
            print()
            print(f'ERROR: Falha no preenchimento.\nRetomando...')
            ROBO.driver.refresh()
            sleep(7)
            ROBO.new_insert()
            ROBO.fill_in_release(
                    row['PLANO'], row['DOCUMENTO'], row['PARTICIPANTE'], \
                    row['EMISSAO'], row['VENCIMENTO'], row['VALOR'], \
                    row['HISTORICO'], row['FORMA DE PAGAMENTO'], row['DATA DE PAGAMENTO']
            )
    else:
        try:
            ROBO.fill_in_release_pg(
                    row['PLANO'], row['DOCUMENTO'], row['PARTICIPANTE'], \
                    row['EMISSAO'], row['VENCIMENTO'], row['VALOR'], \
                    row['HISTORICO'], row['FORMA DE PAGAMENTO'], row['DATA DE PAGAMENTO'], \
                    row['CONTA FINANCEIRA']
            )
        except:
            print()
            print(f'ERROR: Falha no preenchimento.\nRetomando...')
            ROBO.driver.refresh()
            sleep(7)
            ROBO.new_insert()
            ROBO.fill_in_release_pg(
                    row['PLANO'], row['DOCUMENTO'], row['PARTICIPANTE'], \
                    row['EMISSAO'], row['VENCIMENTO'], row['VALOR'], \
                    row['HISTORICO'], row['FORMA DE PAGAMENTO'], row['DATA DE PAGAMENTO'], \
                    row['CONTA FINANCEIRA']
            )

    current_date = datetime.now()
    date_format = current_date.strftime('%d/%m/%Y %H:%M:%S')
    search_loja = ROBO.find_xpath('//*[@id="lblEstabelecimentoSelecionado"]').text
    count += 1

    if count == (i + 1):
        print()
        print(f'{str(count) + "º"} LANCAMENTO ✅')
        print(f'Doc: {row["DOCUMENTO"]} | {search_loja}.')
        print(date_format)
        with open(ROBO.LOG, 'a+') as arquivo:
            arquivo.write(f'{str(count) + "º"} LANCAMENTO OK!\n')
            arquivo.write(f'Doc: {row["DOCUMENTO"]} | {search_loja}.\n')
            arquivo.write(f'{date_format}\n')
            arquivo.write('\n')
            arquivo.write('-' * 20)
            arquivo.write('\n')
    else:
        print(f'ERROR: {str(i) + "º"} LANCAMENTO não realizado! ❌')
        arquivo.write(f'ERROR: {str(i) + "º"} LANCAMENTO não realizado!\n')

        sleep(5)

        print('-' * 20)
        print()


print()
print(f'O total {count} de {ROBO.QNT_LANCAMENTO} LANCAMENTOS foram REALIZADOS!')
print('Enviando e-mail do arquivo!')
ROBO.send_mail(EMAIL, date_format)
ROBO.driver.quit()

import class_robot as cb;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from datetime import datetime
from time import sleep

URL = 'https://app.izzyway.com.br/Account/Login#'
LOGIN, PASSOWORD = '#########', '#######'


robo = cb.RoboIzzyWay()
robo.driver.get(URL)

robo.logar(LOGIN, PASSOWORD)
print('Logando...')
sleep(10)
try:
    robo.modulos('FINANCEIRO')
except:
    robo.driver.refresh()
    print('ERROR: Falha no carregamento!')
    print('Retomando...')
    sleep(10)
    robo.modulos('FINANCEIRO')

print()
print(f'{robo.qnt_lancamento} LANÇAMENTOS existentes!')
print('Realizando lancamentos!')
print()
with open(cb.LOG, 'a+') as arquivo:
        arquivo.write('#' * 30)
        arquivo.write('\n')
        arquivo.write(f'{robo.qnt_lancamento} LANÇAMENTOS existentes!\n')
        arquivo.write('Realizando lancamentos!\n')
        arquivo.write('\n')
        arquivo.write('#' * 30)
        arquivo.write('\n')

count = 0

# LOOP
for i, row in cb.LER.iterrows():
    robo.select_store(row['LOJA'])
    sleep(1)
    robo.new_insert()
    try:
        robo.fill_in_release(
                row['PLANO'], row['DOCUMENTO'], row['PARTICIPANTE'], \
                row['EMISSAO'], row['VENCIMENTO'], row['VALOR'], \
                row['HISTORICO'], row['FORMA DE PAGAMENTO'], row['DATA DE PAGAMENTO']
        )
    except:
        print()
        print(f'ERROR: Falha no preenchimento.\nRetomando...')
        with open(cb.LOG, 'a+') as arquivo:
            arquivo.write('\n')
            arquivo.write(f'ERROR: Falha no preenchimento.\nRetomando...\n')
            arquivo.write('\n')
            arquivo.write('-' * 20)
            arquivo.write('\n')
        robo.driver.refresh()
        sleep(7)
        robo.new_insert()
        robo.fill_in_release(
                row['PLANO'], row['DOCUMENTO'], row['PARTICIPANTE'], \
                row['EMISSAO'], row['VENCIMENTO'], row['VALOR'], \
                row['HISTORICO'], row['FORMA DE PAGAMENTO'], row['DATA DE PAGAMENTO']
        )

    current_date = datetime.now()
    date_format = current_date.strftime('%d/%m/%Y %H:%M:%S')
    search_loja = robo.find_xpath('//*[@id="lblEstabelecimentoSelecionado"]').text
    count += 1

    if count == (i + 1):
        print()
        print(f'{str(count) + "º"} LANCAMENTO ✅  ')
        print(f'Doc: {row["DOCUMENTO"]} | {search_loja}.')
        print(date_format)
        with open(cb.LOG, 'a+') as arquivo:
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
print(f'O total {count} de {robo.qnt_lancamento} LANCAMENTOS foram REALIZADOS!')
robo.driver.quit()


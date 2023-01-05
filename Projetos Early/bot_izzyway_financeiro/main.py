import class_robot as cb;
from time import sleep

URL = 'https://app.izzyway.com.br/Account/Login#'
LOGIN, PASSOWORD = '##########', '#######'


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
print(f'Total de {robo.qnt_lancamento} existentes!')
print('Realizando lancamentos!')
print()
robo.lancamento()
robo.driver.quit()



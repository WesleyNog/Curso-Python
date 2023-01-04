import func as f;
from time import sleep
from selenium.webdriver.common.by import By;

URL = 'https://app.izzyway.com.br/Account/Login#'
LOGIN, PASSOWORD = '############', '##########'


f.driver.get(URL)

f.logar(LOGIN, PASSOWORD)
sleep(10)
try:
    f.modulos('FINANCEIRO')
except:
    f.driver.refresh()
    print('ERROR: Falha no carregamento!')
    print('Retomando...')
    sleep(10)
    f.modulos('FINANCEIRO')
    
try:
    f.lancamento()
    print(f'Todos os lancamentos foram realizados com sucesso!')
except:
    f.driver.refresh()
    print('ERROR: Sem Lançamentos!')
    print('Retomando...')
    sleep(10)
    f.lancamento()


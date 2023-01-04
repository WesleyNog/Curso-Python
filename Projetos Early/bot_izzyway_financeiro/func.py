from time import sleep;
import selenium;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from xpath import modulos_xpaths, lojas_xpaths, cp_xpaths;
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Firefox()
AR_L = 'C:\\Users\\geren\\OneDrive\\Área de Trabalho\\TesteBot.xlsx'
LER = pd.read_excel(AR_L)

class RoboIzzyWay:
    def __init__(self) -> None:
        pass

    
# Fazer Login do usuário
def logar(user, passoword):
    send_login = driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys(user)
    send_pass = driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(passoword, Keys.ENTER)
    

# Escolher o módulo para que aconteça a operação
def modulos(modulo):
    search_modulo = driver.find_element(By.XPATH, '//*[@id="nameModule"]').text

    if search_modulo != modulo.capitalize():
        mod01 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, modulos_xpaths['modulo']))
        )
        mod01.click()
        
        sleep(0.5)

        mod02 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, modulos_xpaths[modulo.lower()]))
        )
        mod02.click()

        sleep(1)

    # Acessar o Contas a Pagar
    access_cp = driver.find_element(By.XPATH, cp_xpaths['contas_pagar']).click()
    sleep(10)


# Acessar a Loja que ira ser feita a operação
def lancamento():
    
    search_loja = driver.find_element(By.XPATH, '//*[@id="lblEstabelecimentoSelecionado"]').text
    count = 0

    # LOOP
    for i, row in LER.iterrows():
        if search_loja != str(row['LOJA']).upper():
            lj01 = driver.find_element(By.XPATH, lojas_xpaths['loja'])
            lj01.click()

            sleep(0.5)

            lj02 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, lojas_xpaths[str(row['LOJA']).lower()]))
            )
            lj02.click()
            
            sleep(10)

        # Adicionar um novo LANCAMENTO do CONTAS A PAGAR
        novo = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, cp_xpaths['novo_cp']))
        )
        novo.click()

        # Lancamento Simples
        simples = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, cp_xpaths['lancamento_simples']))
        )
        simples.click()
        
        plano_contas = driver.find_element(By.XPATH, cp_xpaths['plano_contas']).send_keys(row['PLANO'], Keys.ENTER)
        centro_resultados = driver.find_element(By.XPATH, cp_xpaths['centro_resultados']).send_keys('1', Keys.ENTER)
        documento = driver.find_element(By.XPATH, cp_xpaths['documento']).send_keys(row['DOCUMENTO'], Keys.ENTER)
        participante = driver.find_element(By.XPATH, cp_xpaths['participante']).send_keys(row['PARTICIPANTE'], Keys.ENTER)
        sleep(3)
        emissao = driver.find_element(By.XPATH, cp_xpaths['emissao'])
        emissao.click()
        emissao.clear()
        sleep(1)
        emissao.send_keys(str(row['EMISSAO']))
        vencimento = driver.find_element(By.XPATH, cp_xpaths['vencimento'])
        vencimento.click()
        vencimento.clear()
        sleep(1)
        vencimento.send_keys(str(row['VENCIMENTO']))
        valor = driver.find_element(By.XPATH, cp_xpaths['valor']).send_keys(row['VALOR'], Keys.ENTER)
        historico = driver.find_element(By.XPATH, cp_xpaths['historico']).send_keys(row['HISTORICO'], Keys.ENTER)
        forma_pagamento = driver.find_element(By.XPATH, cp_xpaths['forma_pagamento'])
        forma_pagamento.click()
        sleep(1)
        forma_pagamento.send_keys(row['FORMA DE PAGAMENTO'])
        data_pagamento = driver.find_element(By.XPATH, cp_xpaths['data_pagamento']).send_keys(str(row['DATA DE PAGAMENTO']))
        salvar = driver.find_element(By.XPATH, cp_xpaths['salvar']).click()
        sleep(1)

        #carregando = driver.find_element(By.XPATH, '/html/body/div[5]/h2/h3')
        
        count += 1
        if count > 0:
            print(f'LANCAMENTO {i + 1} OK!')
        else:
            print('ERROR: Lançamento não finalizado.')
        sleep(3)

    print(f'O total de {count} LANCAMENTOS foram REALIZADOS')
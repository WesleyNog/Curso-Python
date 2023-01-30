# Importação dos Módulos
from time import sleep;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from xpath import modulos_xpaths, lojas_xpaths, cp_xpaths;
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


option = webdriver.FirefoxOptions()
#option = webdriver.ChromeOptions()
option.add_argument('--headless')

# Arquivo que será usado para fazer todos os lançamentos necessários
ARQUIVO = 'Y:\\AUTOMAÇÃO\\Contas a Pagar.xlsx'
LER = pd.read_excel(ARQUIVO)
LOG = 'Y:\\AUTOMAÇÃO\\log_contas.txt'


class RoboIzzyWay:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox(options=option)
        #self.driver = webdriver.Chrome(options=option)
        self.qnt_lancamento = len(LER)

    
    # Fazer Login do usuário
    def logar(self, user, passoword):
        send_login = self.driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys(user)
        send_pass = self.driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(passoword, Keys.ENTER)
        

    # Escolher o módulo para que aconteça a operação
    def modulos(self, modulo):
        search_modulo = self.driver.find_element(By.XPATH, '//*[@id="nameModule"]').text

        if search_modulo != str(modulo).capitalize():
            mod01 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, modulos_xpaths['modulo']))
            )
            mod01.click()
            
            sleep(0.5)

            mod02 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, modulos_xpaths[str(modulo).lower()]))
            )
            mod02.click()

            sleep(1)

        # Acessar o Contas a Pagar
        access_cp = self.driver.find_element(By.XPATH, cp_xpaths['contas_pagar']).click()
        sleep(10)
    
    #############TESTANDO MÉDOTO################
    def find_xpath(self, xpath):
        return WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )


    # Acessar a Loja que ira ser feita a operação
    def select_store(self, store):
        search_loja = self.find_xpath('//*[@id="lblEstabelecimentoSelecionado"]').text
        if search_loja != str(store).upper():
            sleep(5)
            lj01 = self.find_xpath(lojas_xpaths['loja']).click()

            sleep(0.5)

            lj02 = self.find_xpath(lojas_xpaths[str(store).lower()]).click()
            
            sleep(10)

    def new_insert(self):        
        try:
            # Adicionar um novo LANCAMENTO do CONTAS A PAGAR
            novo = self.find_xpath(cp_xpaths['novo_cp']).click()
        except TimeoutError:
            sleep(10)
            novo = self.find_xpath(cp_xpaths['novo_cp']).click()

        # Escolha de Lancamento Simples
        simples = self.find_xpath(cp_xpaths['lancamento_simples']).click()
        
        sleep(2)


    def fill_in_release(self, plano, documento, participante, data_emissao, data_vencimento, valor, historico, forma_pgto, data_pgto):
        # Lançamentos em Loop da Planilha em Excel  cp_xpaths['plano_contas']
        
        plano_contas = self.find_xpath(cp_xpaths['plano_contas']).send_keys(plano, Keys.ENTER)
        centro_resultados = self.find_xpath(cp_xpaths['centro_resultados']).send_keys('1', Keys.ENTER)
        documento = self.find_xpath(cp_xpaths['documento']).send_keys(documento, Keys.ENTER)
        participante = self.find_xpath(cp_xpaths['participante']).send_keys(participante, Keys.ENTER)
        sleep(1)
        emissao = self.find_xpath(cp_xpaths['emissao'])
        emissao.click()
        emissao.clear()
        emissao.send_keys(str(data_emissao), Keys.ENTER)
        vencimento = self.find_xpath(cp_xpaths['vencimento'])
        vencimento.click()
        vencimento.clear()
        vencimento.send_keys(str(data_vencimento), Keys.ENTER)
        valor = self.find_xpath(cp_xpaths['valor']).send_keys(valor, Keys.ENTER)
        historico = self.find_xpath(cp_xpaths['historico']).send_keys(historico, Keys.ENTER)
        forma_pagamento = self.find_xpath(cp_xpaths['forma_pagamento'])
        forma_pagamento.click()
        sleep(0.5)
        select_forma_pagamento = self.find_xpath(cp_xpaths['lista_pagamento'].replace('$$NUMBER$$', str(forma_pgto)))
        select_forma_pagamento.click()
        data_pagamento = self.find_xpath(cp_xpaths['data_pagamento']).send_keys(str(data_pgto), Keys.ENTER)
        salvar = self.find_xpath(cp_xpaths['salvar']).click()
        sleep(3)


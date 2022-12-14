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
option.add_argument('--headless')

# Arquivo que será usado para fazer todos os lançamentos necessários
ARQUIVO = 'C:\\Users\\geren\\OneDrive\\Área de Trabalho\\TesteBot.xlsx'
LER = pd.read_excel(ARQUIVO)

class RoboIzzyWay:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
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
        ##search_cp = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/h2').text

        ##if search_cp != 'Contas a Pagar':
        ##    access_cp = self.driver.find_element(By.XPATH, cp_xpaths['contas_pagar']).click()
        sleep(10)


    # Acessar a Loja que ira ser feita a operação
    def lancamento(self):
        
        count = 0
        search_loja = self.driver.find_element(By.XPATH, '//*[@id="lblEstabelecimentoSelecionado"]').text
        # LOOP
        for i, row in LER.iterrows():
            if search_loja != str(row['LOJA']).upper():
                lj01 = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, lojas_xpaths['loja']))
                )
                lj01.click()

                sleep(0.5)

                lj02 = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, lojas_xpaths[str(row['LOJA']).lower()]))
                )
                lj02.click()
                
                sleep(10)
            try:
                # Adicionar um novo LANCAMENTO do CONTAS A PAGAR
                novo = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, cp_xpaths['novo_cp']))
                )
                novo.click()
            except TimeoutError:
                sleep(10)
                novo = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, cp_xpaths['novo_cp']))
                )
                novo.click()

            # Escolha de Lancamento Simples
            simples = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, cp_xpaths['lancamento_simples']))
            )
            simples.click()
            
            sleep(2)

            # Lançamentos em Loop da Planilha em Excel
          
            plano_contas = self.driver.find_element(By.XPATH, cp_xpaths['plano_contas']).send_keys(row['PLANO'], Keys.ENTER)
            centro_resultados = self.driver.find_element(By.XPATH, cp_xpaths['centro_resultados']).send_keys('1', Keys.ENTER)
            documento = self.driver.find_element(By.XPATH, cp_xpaths['documento']).send_keys(row['DOCUMENTO'], Keys.ENTER)
            participante = self.driver.find_element(By.XPATH, cp_xpaths['participante']).send_keys(row['PARTICIPANTE'], Keys.ENTER)
            sleep(1)
            emissao = self.driver.find_element(By.XPATH, cp_xpaths['emissao'])
            emissao.click()
            emissao.clear()
            emissao.send_keys(str(row['EMISSAO']))
            vencimento = self.driver.find_element(By.XPATH, cp_xpaths['vencimento'])
            vencimento.click()
            vencimento.clear()
            vencimento.send_keys(str(row['VENCIMENTO']))
            valor = self.driver.find_element(By.XPATH, cp_xpaths['valor']).send_keys(row['VALOR'], Keys.ENTER)
            historico = self.driver.find_element(By.XPATH, cp_xpaths['historico']).send_keys(row['HISTORICO'], Keys.ENTER)
            forma_pagamento = self.driver.find_element(By.XPATH, cp_xpaths['forma_pagamento'])
            forma_pagamento.click()
            sleep(0.5)
            select_forma_pagamento = self.driver.find_element(By.XPATH, cp_xpaths['lista_pagamento'].replace('$$NUMBER$$', str(row['FORMA DE PAGAMENTO'])))
            select_forma_pagamento.click()
            data_pagamento = self.driver.find_element(By.XPATH, cp_xpaths['data_pagamento']).send_keys(str(row['DATA DE PAGAMENTO']))
            salvar = self.driver.find_element(By.XPATH, cp_xpaths['salvar']).click()
            sleep(3)
            

            ###carregando = self.driver.find_element(By.XPATH, '/html/body/div[5]/h2/h3')
            ###campos_obrigatorios = self.driver.find_element(By.XPATH, '<div class="toast-message">Campo Participante obrigatório</div>')
            ###savo_sucesso = self.driver.find_element(By.XPATH, '<div class="toast-message">Salvo com sucesso</div>')
            
            search_loja = self.driver.find_element(By.XPATH, '//*[@id="lblEstabelecimentoSelecionado"]').text
            count += 1

            if count == (i + 1):
                print(f'{str(count) + "º"} LANCAMENTO ✅ | Nº Doc {row["DOCUMENTO"]}')
                print(f'Lançado na loja do {search_loja}.')
            else:
                print(f'ERROR: {str(i) + "º"} LANCAMENTO não realizado! ❌')

            sleep(5)

            #if self.driver.find_element(By.XPATH, '/html/body/div[5]/h2/h3'):
            #    sleep(1)

        
        print('-' * 20)
        print()
        print(f'O total {count} de {self.qnt_lancamento} LANCAMENTOS foram REALIZADOS!')

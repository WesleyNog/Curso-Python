from dados_caminhos import caminhos
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://app.izzyway.com.br/Account/Login')
time.sleep(1)

def logar(usuario, senha):
    login = driver.find_element(By.XPATH, caminhos['login'])
    login.send_keys(usuario)
    send_senha = driver.find_element(By.XPATH, caminhos['senha'])
    send_senha.send_keys(senha)
    send_senha.send_keys(Keys.ENTER)
    time.sleep(3)


def navegar(type_operacao, type_estoque, set_movimentacao):
    modulo = driver.find_element(By.XPATH, caminhos['modulo'])
    modulo.click()
    time.sleep(1)
    modulo.send_keys(Keys.F2)
    time.sleep(1)
    movimentacao = driver.find_element(By.XPATH, caminhos['movimentacao'])
    time.sleep(1)
    movimentacao.click()
    select_mov = driver.find_element(By.XPATH, caminhos['select_mov'])
    select_mov.send_keys(set_movimentacao)
    time.sleep(1)
    select_mov.send_keys(Keys.ENTER)
    cart1 = driver.find_element(By.XPATH, caminhos['cart1'])
    cart1.click()
    cart2 = driver.find_element(By.XPATH, caminhos['cart2'])
    cart2.click()
    time.sleep(1)
    new = driver.find_element(By.XPATH, caminhos['new'])
    new.click()
    time.sleep(1)
#    emissao = driver.find_element(By.XPATH, '//*[@id="Emissao"]')
#    emissao.send_keys(Keys.BACKSPACE, '27112022')
#    entrada = driver.find_element(By.XPATH, '//*[@id="EntradaSaida"]')
#    entrada.send_keys(Keys.BACKSPACE, '27112022')
    operacao = driver.find_element(By.XPATH, caminhos['operacao'])
    operacao.send_keys(type_operacao)
    operacao.send_keys(Keys.ENTER)
    estoque = driver.find_element(By.XPATH, caminhos['estoque'])
    estoque.send_keys(type_estoque)
    estoque.send_keys(Keys.ENTER)


def mid(fornecedor, produtos, n_nota, quantidade):
    participante = driver.find_element(By.XPATH, caminhos['participante'])
    participante.send_keys(fornecedor)
    time.sleep(1)
    participante.send_keys(Keys.ENTER)
    numero = driver.find_element(By.XPATH, caminhos['numero'])
    numero.send_keys(n_nota)
    produto = driver.find_element(By.XPATH, caminhos['produto'])
    produto.send_keys(produtos)
    time.sleep(1)
    produto.send_keys(Keys.ENTER)
    time.sleep(1)
    qnt = driver.find_element(By.XPATH, caminhos['qnt'])
    qnt.click()
    qnt.send_keys(Keys.CLEAR)
    time.sleep(0.5)
    qnt.send_keys(quantidade)
    time.sleep(1)


def pagamento(pagamento, vencimento):
    fp = driver.find_element(By.XPATH, caminhos['fp']).click()
    venc = driver.find_element(By.XPATH, caminhos['venc']).send_keys(Keys.CLEAR, vencimento)
    qnt_venc = driver.find_element(By.XPATH, caminhos['qnt_venc']).send_keys('1')
    time.sleep(1)
    forma_pgto = driver.find_element(By.XPATH, caminhos['forma_pgto'])
    forma_pgto.click()
    chose_formapgto = driver.find_element(By.XPATH, caminhos['chose_formapgto'])
    chose_formapgto.send_keys(pagamento)
    chose_formapgto.send_keys(Keys.ENTER)
    time.sleep(1)
    

def plano_contas(codigo_cr):
    plano_contas = driver.find_element(By.XPATH, caminhos['plano_contas'])
    plano_contas.click()
    plano = driver.find_element(By.XPATH, caminhos['plano']).click()
    chose_plano = driver.find_element(By.XPATH, caminhos['chose_plano']).send_keys(codigo_cr, Keys.ENTER)
    centro_resultado = driver.find_element(By.XPATH, caminhos['centro_resultado']).click()
    set_centro_resultado = driver.find_element(By.XPATH, caminhos['set_cr']).send_keys('1', Keys.ENTER)
    sair_plano_contas = driver.find_element(By.XPATH, caminhos['sair_plano']).click()
    time.sleep(1)
    save = driver.find_element(By.XPATH, caminhos['save'])
    save.click()
    time.sleep(5)

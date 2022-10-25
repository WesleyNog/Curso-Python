# Importar Recursos
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Parametros de acesso
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contatos = ['Pessoal', 'Amor']
mensagem = 'Olá, isso é apenas um teste!'

# Definir contatos
def buscar_contato(contato):
    campo_pesquisa = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text.selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(keys.ENTER)

for contato in contatos:
    buscar_contato(contato)

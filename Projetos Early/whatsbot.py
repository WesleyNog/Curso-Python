# Importar Recursos
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Parametros de acesso
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

contatos = ['Pessoal', 'Amor']
#mensagem = 'Olá, isso é apenas um teste!'

# Definir contatos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    

def enviar_mensagem(mensagem):
    send_mensseger = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    send_mensseger.send_keys(mensagem)
    send_mensseger.send_keys(Keys.ENTER)
    
#for contato in contatos:
#    buscar_contato(contato)

buscar_contato('Amor')

y = 0
while True:
    if y == 50:
        break

    enviar_mensagem('Te amo!')
    y += 1

enviar_mensagem('E é verdade esse bilhete!')

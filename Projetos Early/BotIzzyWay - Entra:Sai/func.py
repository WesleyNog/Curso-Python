from time import sleep;
import selenium;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.safari.options import Options;
from xpath import xpaths, marketings;

driver = webdriver.Safari()


def logar(user, passoword):
    send_login = driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys(user)
    send_pass = driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(passoword, Keys.ENTER)
    sleep(3)


def loja():
    mod01 = driver.find_element(By.XPATH, xpaths['loja01']).click()
    mod02 = driver.find_element(By.XPATH, xpaths['loja02']).click()
    sleep(3)


def modulo_estoque():
    mod01 = driver.find_element(By.XPATH, xpaths['modulo01']).click()
    mod02 = driver.find_element(By.XPATH, xpaths['modulo02']).click()
    sleep(3)

def acerto_ajuste():
    acerto = driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[63]/a/i').click()
    ajuste = driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[63]/ul/li[5]/a').click()
    sleep(3)


def new_operacion(operacao):
    new = driver.find_element(By.XPATH, xpaths['novo_lancamento']).click()
    if operacao == 'entrada':
        in_doc = driver.find_element(By.XPATH, xpaths['in_doc']).click()
    else:
        out_doc = driver.find_element(By.XPATH, xpaths['out_doc']).click()
    sleep(3)


def data_operation(date, loja, motivos):
    dates = driver.find_element(By.XPATH, xpaths['date'])
    dates.click()
    dates.clear()
    dates.send_keys(date, Keys.ENTER)
    market = driver.find_element(By.XPATH, xpaths['lojas']).click()
    chose_market = driver.find_element(By.XPATH, marketings['riomar']).click()
    setores = driver.find_element(By.XPATH, xpaths['setor'])
    setores.click()
    setores.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
    motivo = driver.find_element(By.XPATH, xpaths['motivo']).send_keys(motivos, Keys.ENTER)
    participante = driver.find_element(By.XPATH, xpaths['participante']).send_keys('0')

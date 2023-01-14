# Selenium - automação web
# webdriver - no Chrome : chromedriver - é importante ver a versão do Chrome
# versão - Ajuda -> Sobre o Google Chrome 
# Colocar o chromedriver dentro da pasta do python3.8

from selenium import webdriver
# Keys - para apertar teclas
from selenium.webdriver,common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

# Entrar no google 
navegador.get('https://www.google.com')

# xpath - código do que tá na tela

navegador.find_element(
  'xpath',
  'inspecionar -> mouse direito no input -> xpath').send_keys('cotação dólar')
navegador.find_element(
  'xpath',
  'inspecionar -> mouse direito no input -> xpath').send_keys(Keys.ENTER)
# Pegar informação na web
cotacao_dolar = navegador.find_element(
  'xpath', 
  'inspecionar -> mouse direito no input -> xpath').get_attribute('data-value')
print(cotacao_dolar)

cotacao_ouro = navegador.find_element('xpath', 'pegar xpath').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

tabela = pd.read_excel('Produtos.xlsx')


# tabela.loc[linha, coluna] = float(cotacao_dolar)
tabela['Moeda'] == 'Dólar'
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)

tabela['Preço de Compra'] = tabela['Cotação'] * tabela['Preço Original']

tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

# Exportar a base de atualizada
  # index = False - não exporta o índice
tabela.to_excel('Novos Produtos.xlsx', index=False)



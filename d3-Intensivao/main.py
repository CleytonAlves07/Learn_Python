import pyautogui
# Para caracteres especiais 
import pyperclip
import time
# Permite trabalhar com um volume grande de informações - olhar documentação para instalar
import pandas

# pyautogui.click - click
# pyautogui.write - escrever
# pyautogui.press - pressionar
# pyautogui.hotkey - atalho
# pyautogui.position - posição de algo na tela - usado para clicar
# pyautogui.scroll - mover tela para cima ou para baixo

# Abrindo um arquivo - exemplo 
pyautogui.press('win')
pyautogui.write('excel')
pyautogui.press('win')

# Faz os comandos irem mais devagar e ajuda a funcionar
pyautogui.PAUSE = 1

# Passo 1 - Entrar no sistema da empresa
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('endereço aqui')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Ajuda a fazer pausas maiores 
time.sleep(5)

# Passo 2 - Navegar até o local do relatório
time.sleep(5)
print(pyautogui.position())
# clicar com o botão direito pyautogui.click(x=452, y=334, clicks=2 button='right')
pyautogui.click(x=452, y=334, clicks=2)
time.sleep(2)

# Passo 3 - Exportar o relatório (fazer download)
time.sleep(5)
print(pyautogui.position())
pyautogui.click('colocar posição')
pyautogui.click('colocar posição')
pyautogui.click('colocar posição')
time.sleep(5)
# Passo 4 - Calcular os indicadores (faturamento e quantidade de produtos)
# r = raw - avisa que não é caracteres especiais
tabela = pandas.read_excel(r'C:\User\seila\Vendas - dez.xlsx')

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()


# Passo 5 - Enviar e-mail
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('endereço aqui')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')

pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = f"""
Prezados, bom dia 

O faturamento de ontem foi: R$ {faturamento:,.2f}
A quantida de produtos foi de: R$ {quantidade:,.2f}

abs
Cleyton Alves"""

pyperclip.copy(texto)
payutogui.hotkey('ctrl', 'v')

payautogui.hotkey('ctrl', 'enter')





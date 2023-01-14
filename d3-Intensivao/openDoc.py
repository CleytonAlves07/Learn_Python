import pyautogui as pa
import pyperclip
import time
import pandas as pd


# Abrir arquivo excel

pa.PAUSE = 3

pa.hotkey('win', 'a')
pa.write('Google')
pa.press('enter')
pyperclip.copy('https://drive.google.com/drive/my-drive')
pa.hotkey('ctrl', 'v')
pa.press('enter')
pa.click(x=900, y=1482, clicks=2)
pa.click(x=914, y=966, clicks=2)

tabela = pd.read_excel(r'/home/sette/Downloads/Vendas - Dez.xlsx')


faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

# Enviando resumo do faturamento via e-mail

texto = f"""
Prezados, bom dia! 

Segue abaixo um resumo dos resultados de ontem:

O faturamento foi de: {faturamento:,.2f}
A quantidade de itens vendidos foi de {quantidade:,.2f}

Fico a disposição para maiores esclarecimentos,
"""

pa.hotkey('ctrl', 't')
time.sleep(5)
pa.click(x=3344, y=422)
time.sleep(1)
pa.click(x=392, y=554)
time.sleep(3)
pa.write('cleyton.alves.a@gmail.com')
pa.press('tab')
pa.press('tab')
pyperclip.copy('Relatório diário de vendas')
pa.hotkey('ctrl', 'v')
pa.press('tab')
pyperclip.copy(texto)
pa.hotkey('ctrl', 'v')
pa.click(x=2409, y=2073)



# time.sleep(3)
# print(pa.position())



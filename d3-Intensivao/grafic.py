# Para instalar o pandas no VSCode é necessário instalar também o numpy e o openpyx1
import pandas as pd
# Cria gráficos
import plotly.express as px

# 1 - Importar a base de dados
  # o r é para ele não considerar os / do caminho como caracteres especiais 
  # sheets diz qual a aba que você quer no excel - default aba 1
# tabela = pd.read_csv(r'/home/sette/Downloads/telecom_users.csv', sheets=1)
tabela = pd.read_csv(r'/home/sette/Downloads/telecom_users.csv')

# axis -> 0 = linha ; axis -> 1 = coluna 
# Excluindo uma coluna -  drop(nome da coluna, axis=1)
  # Excluindo várias colunas - drop(['coluna1', 'coluna2'])
# Excluindo uma linha - drop(nº da linha, axis=0)

tabela = tabela.drop('Unnamed: 0', axis=1)

# print(tabela.info()) - Resumo da tabela - bem útil 

# Modificar os valores que estão com um type errado
  # Alterar tipo de dados no pandas
    # https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

  # errors{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
    # If 'raise', then invalid parsing will raise an exception.
    # If 'coerce', then invalid parsing will be set as NaT.
    # If 'ignore', then invalid parsing will return the input.
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# Tratando os valores vazios 
  # Excluir as colunas que todos os valores estão vazio
    # dropna(how='all') - todos os valores vazios
    # dropna(how='any') - pelo menos um valor vazio
    # axis=1 - coluna
tabela = tabela.dropna(how='all', axis=1)


  # Excluir linhas que tem pelo menos 1 valor vazio
    # axis=0 - linha
tabela = tabela.dropna(how='any', axis=0)

# Saber quantos canceleram 
  # .sum() - somar
  # .mean() - média
  # .value_counts() - contar valores
# print(tabela['Churn'].value_counts()) - mostra quantos em valores
# print(tabela['Churn'].value_counts(normalize=True)) - mostra em percentual
# .map("{:.1%}".format) - formatar - ex: 26%
print(tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format))

# Comparar as colunas com o Churn
  # Criar o gráfico
coluna = 'TipoContrato'
    # color='Churn' - faz uma diferença de cor de acordo com o cancelamento
    # px.histogram
grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True) 
# grafico.show()
  # Exibir o gráfico
    #grafico.show()

  # Criar um gráfico para cada coluna na tabela 
for coluna in tabela.columns:
  grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True) 
  grafico.show()





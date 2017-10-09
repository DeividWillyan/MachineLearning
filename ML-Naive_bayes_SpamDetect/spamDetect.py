import pandas as pd

# Importe o conjunto de dados para um banco de dados de pandas usando o método read_table.
# Como este é um conjunto de dados separado por tabulação, usaremos '\ t' como o valor
# para o argumento 'sep' que especifica esse formato.
# Além disso, renomeie os nomes das colunas especificando uma lista ['label,' sms_message ']
# para o argumento' names 'de read_table ().
df = pd.read_table('SMSSpamCollection',
                   sep='\t',
                   header=None,
                   names=['label', 'sms_message'])

# Converta os valores na coluna 'label' em valores numéricos usando o método de mapa da seguinte forma:
# {'ham': 0, 'spam': 1} Isso mapeia o valor 'ham' para 0 eo valor 'spam' para 1.
df['label'] = df.label.map({'ham':0, 'spam':1})

# Além disso, para ter uma idéia do tamanho do conjunto de dados com o qual estamos lidando,
#  imprima o número de linhas e colunas usando 'shape'.
print("Quantidade de Linha, Colunas: ", df.shape)

# Imprima o primeiro valor do dataframe com os novos nomes das colunas.
print(df.head(1))



# Agora iremos implementar o algoritimo Bag Of Words (BoW) utilizando a biblioteca scikit-learn de forma mais simplificada.

# (1) criamos nosso documento com 4 frases.
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

# (2) Importe o método sklearn.feature_extraction.text.CountVectorizer e crie uma instância chamada 'count_vector'.
from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()

# (3) Ajustar o conjunto de dados do documento ao objeto CountVectorizer que você criou usando fit()
#     E obtenha a lista de palavras que foram categorizadas como recursos usando o método get_feature_names().
count_vector.fit(documents)
#print(count_vector.get_feature_names())

# (4) Crie uma matriz com as linhas sendo cada um dos 4 documentos e as colunas sendo cada palavra.
#     O valor correspondente (linha, coluna) é a freqüência de ocorrência dessa palavra (na coluna) em um
#     documento específico (na linha). ocê pode fazer isso usando o método transform () e passando no conjunto
#     de dados do documento como o argumento. O método transform () retorna uma matriz de números inteiros numpy,
#     você pode converter isso em uma matriz usando toarray (). Chame a matriz 'doc_array'
doc_array = count_vector.transform(documents).toarray()
# print(doc_array)


# (5) Converta a matriz que obtivemos, carregada em 'doc_array', em um dataframe e configure os nomes das colunas
#     para os nomes das palavras (que você calculou anteriormente usando get_feature_names (). Ligue para o
#     quadro de dados 'frequency_matrix'.
import pandas as pd

frequency_matrix = pd.DataFrame(doc_array,
                                columns=count_vector.get_feature_names())
#print(frequency_matrix)

# (6) Divida o conjunto de dados em um conjunto de treinamento e teste usando o método train_test_split no sklearn.
#     Divida os dados usando as seguintes variáveis:
#     X_train é o nosso dados de treinamento para a coluna 'sms_message'
#     y_train são nossos dados de treinamento para a coluna 'etiqueta'
#     X_test é o nosso dado de teste para a coluna 'sms_message'.
#     y_test é o nosso dado de teste para a coluna 'etiqueta' Imprima o número de linhas
#       que temos em cada um dos nossos dados de treinamento e teste.

from sklearn.model_selection import train_test_split

# lendo o SMSSpamCollection
df = pd.read_table('../SMSSpamCollection',
                   sep='\t',
                   header=None,
                   names=['label', 'sms_message'])


# deivid, transformando ham e spam como 0 e 1
encoded_labels = df['label'].map(lambda x: 1 if x == 'spam' else 0).values

X_train, X_test, y_train, y_test = train_test_split(df['sms_message'],
                                                    encoded_labels)

# print('Número de linhas no conjunto total: {}'.format(df.shape[0]))
# print('Número de linhas no conjunto de treinamento: {}'.format(X_train.shape[0]))
# print('Número de linhas no conjunto de teste:  {}'.format(X_test.shape[0]))

# (7) Aplicando o processamento do Bag of Words ao nosso conjunto de dados.

count_vector = CountVectorizer()
training_data = count_vector.fit_transform(X_train)
testing_data = count_vector.transform(X_test)

# (8) Implementação do teorema de Bayes a partir do zero.

"""
Agora que temos nosso conjunto de dados no formato que precisamos, podemos passar para a próxima parcela da nossa missão, 
que é o algoritmo que usamos para fazer nossas previsões classificar uma mensagem como spam ou não spam. Lembre-se que, 
no início da missão, discutimos brevemente o teorema de Bayes, mas agora vamos abordar um pouco mais. Em termos leigos, 
o teorema de Bayes calcula a probabilidade de ocorrência de um evento, com base em certas outras probabilidades relacionadas
ao evento em questão. É composto de um prévio (as probabilidades de que estamos cientes ou que nos é dado) e o posterior
(as probabilidades que estamos buscando para calcular usando os priores).

Carregamos os dados de treinamento na variável 'training_data' e os dados de teste no variável 'testing_data'.
Importe o classificador MultinomialNB e ajuste os dados de treinamento no classificador usando fit (). 
"""

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)
# print(naive_bayes)


# (9) Agora que nosso algoritmo foi treinado usando o conjunto de dados de treinamento, podemos agora fazer algumas
#     previsões nos dados do teste armazenado em 'testing_data' usando predict ()

predictions = naive_bayes.predict(testing_data)
#print (predictions)

"""
Para problemas de classificação que estão distorcidos em suas distribuições de classificação, como em nosso caso, por exemplo,
se tivéssemos 100 mensagens de texto e apenas 2 fossem spam e o restante 98 não fosse, a precisão por si só não é uma métrica 
muito boa. Poderíamos classificar 90 mensagens como não spam (incluindo as 2 que eram spam, mas classificá-las como não spam, 
portanto, seriam falsas negativas) e 10 como spam (todos os 10 falsos positivos) e ainda obter uma nota de precisão 
razoavelmente boa. Para tais casos, a precisão e a lembrança são úteis. Essas duas métricas podem ser combinadas para obter 
o escore F1, que é a média ponderada da precisão e os resultados da recuperação. Esta pontuação pode variar de 0 a 1, 
sendo 1 o melhor resultado F1.
Vamos usar todas as 4 métricas para garantir que nosso modelo seja bem. Para todas as 4 métricas cujos valores podem 
variar de 0 a 1, ter uma pontuação tão próxima de 1 quanto possível é um bom indicador de quão bem o nosso modelo está fazendo.
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
print('Precision score: ', format(precision_score(y_test, predictions)))
print('Recall score: ', format(recall_score(y_test, predictions)))
print('F1 score: ', format(f1_score(y_test, predictions)))

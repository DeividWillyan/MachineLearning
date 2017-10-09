# Passo a passo para a implementação do Algoritiomo/Processo "Bag of Words" (BoW),
# este processo deve pegar um texto como input e realizar algumas etapas como, converter todas a palavras para minusculas,
# remover a pontuação e acentuação na frase, realiza o procedimento de tokenization que seria transformar uma frase(linha)
# em uma lista de strings para cada palavra da frase, e por ultimo realizar o processo de contar a frequencia que
# cada palavra aparece no texto (input) de entrada.


# (1) Aqui pegamos um texto com letras Maiusculas e Minusculas e convertemos todas para minuscula.
#     Criamos a lista lower_case_documents e adicionamos o resultado da conversao nela.
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())
#print(lower_case_documents)


# (2) Neste segundo passo removemos toda a acentuação e adinicionamos em uma lista sans_punctuation_documents
sans_punctuation_documents = []
import string

for i in lower_case_documents:
    sans_punctuation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))
#print(sans_punctuation_documents)


# (3) Nesta etapa de Tokenization nós pegamos as palavras do sans_punctuation_documents realizamos uma tecnica
#     para converter as frases em uma matrix de [frase X palavras], ou seja, pegamos uma frase e realizamos um split
#     com o delimitador espaço (' ') e e adicionamos o array de palavras da frase na lista preprocessed_documents.
preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split(' '))
#print(preprocessed_documents)


# (4) O contador conta a ocorrência de cada item na lista e retorna um dicionário
#     com a chave como o item sendo contado eo valor correspondente sendo a contagem desse item na lista.
frequency_list = []
import pprint
from collections import Counter

for i in preprocessed_documents:
    frequency_counts = Counter(i)
    frequency_list.append(frequency_counts)
pprint.pprint(frequency_list)



# (1) Aqui pegamos um texto com letras Maiusculas e Minusculas e convertemos todas para minuscula
#     Cria,ps a lista lower_case_documents e adicionamos o resultado da conversao nela.
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
print(preprocessed_documents)


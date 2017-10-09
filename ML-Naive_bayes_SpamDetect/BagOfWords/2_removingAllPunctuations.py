
#Aqui pegamos um texto com letras Maiusculas e Minusculas e convertemos todas para minuscula
# Cria,ps a lista lower_case_documents e adicionamos o resultado da conversao nela.
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())


# Neste segundo passo removemos toda a acentuação e adinicionamos em uma lista sans_punctuation_documents
sans_punctuation_documents = []
import string

for i in lower_case_documents:
    sans_punctuation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))
print(sans_punctuation_documents)
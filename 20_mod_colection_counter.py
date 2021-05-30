"""
Módulo Collections -  Counter (Contador)

Collections -  High Performance Container Datatypes

Counter  - Recebe um interavel como parâmetro e cria um objeto do tipo collections Counter que é parecido
com um dicionário, contendo como chava o elemento da lista passada com parâmetro e como
valor a quantidade de ocorrências desse elemento.


# Realizando o Import


# Exemplo 1
from collections import Counter

# Podemos utilizar qualuqer iterável,  aqui usamos uma lista
lista = [1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 34, 23, 56]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({3: 5, 1: 4, 2: 3, 4: 3, 5: 2, 34: 1, 23: 1, 56: 1})

# Veja que para cada elemento da lista, o Counter  criou uma chave e colocou como
# valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})



"""

from collections import Counter

# Exemplo 3


texto = """O território que atualmente forma o Brasil foi encontrado pelos portugueses em 1500, 
durante uma expedição liderada por Pedro Álvares Cabral. 
A região, que até então era habitada por indígenas ameríndios divididos entre milhares de grupos 
étnicos e linguísticos diferentes, torna-se uma colônia do Império Português. O vínculo colonial foi rompido, 
de fato, quando em 1808 a capital do reino foi transferida de Lisboa para a cidade do Rio de Janeiro, 
depois de tropas francesas comandadas por Napoleão Bonaparte invadirem o território português.  """

palavras = texto.split()

# print(palavras)

res = Counter(palavras)


# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(10))


"""

Módulo Collections - Named Tuple


# Backup Tupla
tupla = {1, 2, 3}

print(tupla[1])


Named Tuple - > São tuplas diferenciadas onde, especificamos um nome para a mesmas e também parâmetros.
"""

# Importando

from collections import  namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 -  Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 -   Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 -   Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])


# Usando Named Tuple

ray = cachorro(idade=2, raça='Chow Chow', nome='ray')

print(ray)

# Acessando os dados
# Forma 1


print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome


# Forma 2
print(ray.idade)  # idade
print(ray.raça)  # raça
print(ray.nome)  # nome




print(ray.index('Chow Chow'))  # índice
print(ray.count('Chow Chow'))  # contar






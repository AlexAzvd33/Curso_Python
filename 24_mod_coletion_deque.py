"""
Módulo Collections  - Deque

Podemos dizer que o Deque é uma lista de alta performance
( é o mais parecido com uma lista )

"""

# Importando

from collections import deque

# Criando deques


deq = deque('Geek')

print(deq)


# Adicionando elementos no deque

deq.append('y') # Adiciona no final

print(deq)

deq.appendleft('k') # Adiciona no começo

print(deq)


print(deq.pop()) # Remove e  retorna o ultimo elemento

print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento.

print(deq)







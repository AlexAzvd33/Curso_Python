"""
Tipo  String

Já vimos que em Python, um dado é considerado do tipo string(), sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas ->''uma string'', ''234'', ''a'', ''True'', ''42.3''
- Estiver entre àspas simples triplas ->'''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome= 'Angelina \nJolie'
print(nome)
print(type(nome))


nome = 'Angelina \* Jolie'
print(nome)
print(type(nome))

print(nome.upper()) # Letras maiusculas

print(nome.lower()) # Letras minusculas

print(nome.split()) # Transforma em lista de strings

nome = 'Geek University'
print(nome[0:4])#Slice de string

print(nome[5:15])#Slice de string

print(nome.split()[1])

"""
# Estiver entre àspas duplas triplas - > """uma string""",  """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,  4,   5,  6,  7,  8,  9,  10, 11, 12, 13, 14]
# ['G', 'e', 'e', 'k',' '  'U','n','i','v','e','r','s','i','t','y']
nome = 'Geek University'

"""
[:: -1 ]Comece do primeiro elemento, vá até o ultimo elemento e inverta
"""
print(nome[::-1]) # Inversão da String, modo Pythônico

print(nome.replace('e', 'i'))

print(type(nome))

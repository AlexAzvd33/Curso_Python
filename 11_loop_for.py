"""
Loop for

Loop --> é uma estrutura de repetição.
For --> uma destas estruturas.

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
  nome = 'Geek University'
- Lista
  lista = [ 1, 3, 5, 7]
-Range
  numeros =  range (1,10)


****** inicio********
nome = 'Geek Universtity'
lista = [ 1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

  #Exemplo de for  1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)
OBS: O valor final não é 'inclusive'(inclusivo) -  de  1, 10, o ultimo valor, será  o 9, e não  o  numero 10.

for numero in range(1, 10):
    print(numero)


    Enumerate:

((0, 'G'), (1, 'e'),  (2, 'e'), (3, 'k')....)
for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome): # o  _, serve para descartar um valor que não será utilizado.
    print(letra)

for valor in enumerate(nome):
    print(valor)

# Resultado
# (0, 'G')
# (1, 'e')
#(2, 'e')
#3, 'k')
# ...



qtd = int(input('Quantas vezes este loop deve rodar? '))

for n in range(1, qtd+1):
    print(f'Impriminfo {n}')

for n in range(1, qtd+1):
    num =  int(input(f'Informe o  {n}/{qtd} valor: '))
    soma  = soma + num
print(f'A soma é {soma}')


nome =  'Geek University'
for letra in nome:
    print(letra, end='')


Tabela de  Emojis Unicode:
https://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F60D
# Modificado: U0001F60D

for num in range(1, 11):
    print('\U0001F60D * num')

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

_________________________________________________________________

# Original: U+1F605
# Modificado: U0001F605

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F605' * num)

"""








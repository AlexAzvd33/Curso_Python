"""
Escopo de Variáveis

Dois casos de escopo:

1 -  Variáveis globais;
   - São reconhecidas, ou seja, seu escopo compreende, todo o programa.


2 - Variáveis locais;
    -  Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.


Para declarar variáveis em Python, fazemos:

nome_da_variavel = valor_da_variavel

Python é uma liguagem de tipagem dinâmica. Isso significa que ao
declararmos uma variàvel, nós não colomos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.
"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))


numero = 42
 # novo = 0

if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada localmente dentro do bloco do if. Portanto é local
    print(novo)

print(novo)


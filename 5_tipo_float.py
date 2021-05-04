"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a virgula.
"""
# Errado do ponto de vista do Float, mas gera uma Tupla.
valor = 1, 44
print(valor)
print(type(valor)) ## tupla

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))## float


# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1)) ## inteiro
##print(valor2)
##print(type(valor2) ## inteiro

# Podemos converter um Float para um Int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabaljhar com números complexos
variavel = 5j


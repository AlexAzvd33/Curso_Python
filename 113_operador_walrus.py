"""
O operador Walrus, permite fazer a atribuição e retorno de valor em uma única expressão.


variável := expressão

EX. 01:

nome = 'Geek University'
print(nome)

print(nome := 'Geek Universtiy")


-------> Python 3.7
# EX.  02

cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta =  input('Informe a fruta: ')


"""


#Python 3.8

cesta = []
while (fruta := input('Informe a fruta: '))  != 'jaca':
    cesta.append(fruta)

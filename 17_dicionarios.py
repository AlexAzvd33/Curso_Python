"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python, são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

Ex:  print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos  - > 'chave':'valor';
    - Tanto chave quanto valor podem ser de  qualquer tipo de dado;
    - Podemos misturar tipos de dados;



####  Criação de dicionários  ####

# Forma 1 - (Mais comum )

paises = {'br': 'Brasil', 'eua': 'Estudos Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 ( Menos comum )

paises = dict(br='Brasil', eua='Estudos Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla.
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentammos fazer o acesso utilizando uma chave que não existe, teremos o 'KeyError'.

# Forma 2 - Acessando via get - Recomendado***

print(paises.get('br'))
print(paises.get('ru'))

___________________________________________________________________________
# Caso o get não encontre o objeto com a chave informada, será retornado o valor None.
Enão será gerado 'KeyError'
país = paises.get('ru')

if país:
    print(f'Encontrei o país, {país}!')
else:
    print('Não encontrei o país.')

____________________________________________________________________________

# Podemos definir u valor padrão para caso não encontremos o objeto com a chave informada.
país = paises.get('py', 'Não encontrado.')

print(f'Encontrei o país, {país}!')



# Podemos verificar se determinada chave se encontra em um dicionário.
print('br' in paises)
print('ru'in paises)
print('Estados Unidos' in paises)


if 'ru' in paises:
    russia = paises['ru']
#  Podemos utilizar qualquer tipo de dado inclusive [ int, float, string, boolean], inclusive lista,
#  tupla, dicicionário como chaves de dicionários.

# OBS: Tuplas por exemplo bastante  interessantes de serem utilizadas como chave de dicionários, pois
# as mesmas são imutáveis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova Iorque',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))


# Forma 1 - Mais Comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'maio': 500}

receita.update(novo_dado)  # receita.update({'mai':500})

print(receita)


#  Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)


# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas. Caso isso acontece, os valores serão subescritos.


# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1 -  Mais comum
ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento um KeyError é  retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é retornado.



# Forma 2

del receita['fev']

print(receita)

#  Se a chave não existir será gerado um KeyError.
#  Neste caso, o valor removido não é retornado.
"""

#  Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras, onde adicionamos produtos.

"""
Carrinho de Compras: 
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# 1- Poderíamos utilizar uma lista  para  amazenarmos estas informações


carrinho = []
produto1 = ['Playstation4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]


carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 -  Poderíamos utilizar uma tupla para isso?  Sim.

produto1 = ('Playstation4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar um dicionário para isso? Sim.

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God Of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos produtos no carrinho e em cada produto 
# podemos ter a certeza  sobre cada informação.


##### Métodos de dicionário

d = dict( a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário ( Zerar dados)

d.clear()
print(d)

# Copiando um dicionário para outro
# Forma 1   - Deep copy  

novo = d.copy()  # Deep copy  

print(novo)

novo['d'] = 4

print(d)
print(novo)


# Forma 2  - Shallow copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)


# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# OBS: O método "fromkeys" recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.


veja = {}.fromkeys('teste', 'valor')
print(veja)


veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)


"""



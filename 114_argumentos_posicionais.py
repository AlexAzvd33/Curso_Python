"""
Argumentos somente Posicionais

"""

# valor = '67.3'
# print(float(valor))

#def cumprimenta_v1(nome):
#   return f'olá {nome}'


#print(cumprimenta_v1('Geek'))


def cumprimenta_v2(nome,  /):
    return  f'Olá {nome}'

print(cumprimenta_v2('Geek'))
print(cumprimenta_v2(nome='Geek'))



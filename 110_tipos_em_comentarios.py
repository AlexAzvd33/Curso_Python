"""
Tipos em comentários
Colocamos logo abaixo da função, podemos colocar o tipo do dado, como comentário.

"""

import math

def circunferencia(raio):
    #type: (float) ->float
    return  2 * math.pi * raio

#print(circunferencia(8))

# print(circunferencia('geek'))

def cabecalho1(texto, alinhamento=True):
    #type: ( str, bool) ->str
    if alinhamento:
      return 'a'
    else:
      return  'b'



def cabecalho2(
        texto,  # type: str
        alinhamento=True # type: bool
): # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto='42', alinhamento=False)
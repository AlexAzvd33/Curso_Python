"""
PEP8 -  Python Enhancement Proposal

São propostas de melhorias  para a linguagem  Python

The Zen of Python

*import this*

A ideia da PEP8 é que possamos escrever códigos Python de forma "pythônica"


[1]  - Utilize Camel Case para nomes de classes;

ex:
class Calculadora: -- > correto
    pass

class calculadora_cientifica: -- > errado
    pass
*********************************************
[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
     pass

numero = 4

numero_impar = 5
**********************************************
[3]  - Utilize 4 espaços para identação! ( NÃO USE TAB)

if 'a' in 'banana':
    print('tem')


[4] -  Linhas em branco
-Separar funcões e definições de classe com duas linhas em branco;
- Métodos denro de uma classe devem ser seprados com uma única linha me branco;

class Classe:
   pass
>> 1 linha em branco
>> 2 linha em branco

[5]  - Imports
- Imports devem ser sempre feitos em linhas separadas;

#Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.


[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ]. { outro: 2 } )

#Faça:

funcao(algo[1]. {outro: 2})

[7] - Termine sempre uma instrução, com uma nova linha
"""



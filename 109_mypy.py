"""
MY PY


def cabecalho(texto: str,  alinhamento: bool = True) -> str: ## função retorna uma string
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return  f"{texto.title()}" .center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento=True))


Usando MYPY:
Podemos usar o comando no terminal : mypy  nome_do_arquivo.py



# Correto

texto: str

) -> str

#Incorreto

texto:str
texto  : str

)->str



import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

# print(circunferencia.__annotations__)

nome: str  = 'Geek University'

peso: float = 67.9

ativo: bool  = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)


Resposta: 
Geek University
67.9
True
{'nome': <class 'str'>, 'peso': <class 'float'>, 'ativo': <class 'bool'>}
"""

class Pessoa:

    def __int__(self, nome: str, idade: int,  peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome}  está andando'

p = Pessoa(nome='Geek University', idade=37, peso=69.5)

print(p.__dict__)

print(p.__annotations__)
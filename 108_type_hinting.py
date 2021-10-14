"""
Type Hinting


////exemplo 01 //
def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'

print(cumprimentar('Geek'))


////exemplo 02 //
def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return  f"{texto.title()}" .center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))



////exemplo  03 //

def cabecalho(texto: str,  alinhamento: bool = True) -> str: ## função retorna uma string
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return  f"{texto.title()}" .center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))


"""
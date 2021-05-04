"""
Estrturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
   - not

Operadores binários:
   - and, or, is

Exemplo de NOT:
ativo = False
logado =  False

#Se não estiver ativo
if  not ativo:
    print('Você precisa ativar a sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print(not False)
********************************************************************************************
Exemplo de IS:


___________________________________________________________________________________________________________

- REGRAS DE FUNCIONAMENTO:
Para o 'and', ambos os valores precisam ser True.
Para o 'or", um outro valor, precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False. Se for False, será True.
Para o 'is', o  valor é  comparado com um segundo.
___________________________________________________________________________________________________________
Exemplo  de  AND:
ativo = True
logado =  True

if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

**********************************************************************************************
Exemplo de  OR:
ativo = True
logado =  False

if ativo or logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
***********************************************************************************************
"""
ativo = True
logado =  False

#Se não estiver ativo
if ativo is False:
    print('Bem-vindo usuário')

else:
    print('Você precisa ativar a sua conta. Por favor, cheque seu e-mail')

#ativo é verdadeiro?
print(ativo is True)


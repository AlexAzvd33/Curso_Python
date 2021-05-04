"""
Estruturas condicionais
If, else, elif
"""

#idade = 18

idade = int(input('Qual a sua idade: '))

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 11:
    print('Tem 11 anos')
else:
    print('Maior de idade')



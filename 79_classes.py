"""
POO - Classes

Em POO, Classes nada mais são que modelos dos objetos do mundo real representados.
Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.


Classes podem conter:
   - Atributos --> representam as caracteristicas do o objeto, ou seja, pelos atributos conseguimos
   representar computacionalmente os estados de um objto. No caso da lâmpada, possivelmente
   iríamos querer saber se a lâmpada é  110 ou 220 volts, se ela é branca, amarela, vermelha ou
   outra cor, qual a luminosidade dela e etc.

   - Médotos ( funções) --> Representam os comportamentos do objeto, ou seja, as ações uq este
   objetos pode realizar em seu sistema, no caso da lâmpada, por exemplo, um comportamento comum
   que muito povavelmente iriamos queere representar no nosso sistema é o de ligar e desligar a
   mesma.


Em Pyhton, para definirmos uma classe utilizamos a palavra reservada class.


OBS: Utilizamos a palavra ***pass***, quando temos um bloco de código que ainda não está
implementado.

OBS:Quando nomeamos **nossas classes** em Python utilizamos por convenção o nome com a inicial
em maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em
maiúsculo, todas juntas.


Dica Geek: Em computação não utilizamos: Acentuação, caractres especiais, espaços ou similares
para nomes de classes, atributos, métodos, arquivos, diretórios e etc.

Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamois
estes objetos que serão mapeados para classes de entidade
"""

class lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass

lamp = lampada() ## criando a classe da lampada

print(type(lamp))


valor = int('42')  # cast

print(help(int))
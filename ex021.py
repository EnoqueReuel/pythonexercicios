'''Um professor quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''
import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))


'''Um Pai quer escolher um dos seus 4 filhos mais velhos para ajudá-lo
   a carregar 1/2m de areia. Faça um programa que o ajude, lendo o
   nome dele e escrevendo o nome escolhido.'''

import random
son1 = str(input('First son:'))
son2 = str(input('Secund son:'))
son3 = str(input('Third son:'))
son4 = str(input('Bedroom son:'))
list = [son1,son2,son3,son4]
chosen = random.choice(list)
print('The chosen son was {}'.format(chosen))

'''Uma mãe quer escolher umas de sua 3 filhas para ir ao mercado.
   Faça um programa que a ajude, lendo o nome delas e escrevendo
   o nome escolhido.'''
import random
f1 = str(input('Primeira filha:'))
f2 = str(input('Segunda filha:'))
f3 = str(input('Terceira filha:'))
lista = [f1, f2, f3]
escolhida = random.choice(lista)
print('A filha escolhida para ir ao mercado é: {}'.format(escolhida))


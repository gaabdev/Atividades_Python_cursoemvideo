#Author: Gabriel Silva
#Date: 21/09/2021

#Algoritmo que soeteia entre quatro alunos, o nome de um  para apagar a lousa.
import random

alunos = ['Harry', 'Hermione', 'Rony', 'Draco']
sorteioaluno = random.choice((alunos))

print('O aluno escolhido para apagar a lousa é... {}.'.format(alunos))
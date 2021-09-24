#Author: Gabriel Silva
#Date: 21/09/2021

#Algoritmo que Sorteie a ordem de apresentação de quatro alunos

import random


alunos = ['Harry', 'Hermione', 'Draco', 'Rony']

escolhido = random.choice(alunos)
print('O primeiro aluno a apresentar será... {}.'.format(escolhido))

apresentacao2 = 
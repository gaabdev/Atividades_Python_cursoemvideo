#Author: Gabriel Silva
#Date: 14/09/2021

#Algoritmo que recebe duas notas do aluno e calcula a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2

print('>'*50)
print(f'Suas notas foram {nota1} e {nota2}, respectivamente.')
print('>' *50)
print(f'A sua média é de {media}')
print('>'*50)
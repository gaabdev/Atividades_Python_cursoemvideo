#Author: Gabriel Silva
#Date: 14/09/2021

#Programa que mostra o sucessor e o antecessor de um número inteiro aleatório.

numeroaleatorio = int(input('Digite um número: '))
sucessor = numeroaleatorio + 1
antecessor = numeroaleatorio - 1

print('>' *30)
print(f'Número digitado: {numeroaleatorio}')
print('>' *30)
print(f'Sucessor: {sucessor}')
print('>' *30)
print(f'Antecessor: {antecessor}')
print('>' *30)
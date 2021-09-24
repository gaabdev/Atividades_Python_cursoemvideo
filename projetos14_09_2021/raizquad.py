#Author: Gabriel Silva
#Date: 14/09/2021

#Algoritmo que leia um número e mostre o dobro, triplo e raiz quadrada do mesmo

import math

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizq = math.sqrt(numero) 

print('>' *30)
print(f'O dobro do número {numero} é {dobro}.')
print('>' *30)
print(f'O triplo do número {numero} é {triplo}')
print('>' *30)
print(f'A raiz quadrada de {numero} é {raizq}')
print('>' *30)
#Author: Gabriel Silva
#Date: 16/09/2021

#Peograma que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, trunc

a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjascente: '))

catetoA = a **2
catetoB = b **2
hipotenusa = catetoA + catetoB

print('O valor da hipitenusa é {}.'.format(trunc(sqrt(hipotenusa))))

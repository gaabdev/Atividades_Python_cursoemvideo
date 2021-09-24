#Author: Gabriel Silva
#Date: 15/09/2021

#Algoritmo que leia a altura e largura de uma parede em metros e calcule quantidade de tinta necessária  para pinta- la. sabendo que 1 litro pinta uma área de 2 m².

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

metrosquadrados = largura * altura
litrotinta = metrosquadrados / 2
print('Esta parede é de {} metros quadrados.'.format(metrosquadrados))
print('Serão necessário(s) {} litro(s) de tinta, para pinta- la.'.format(litrotinta))
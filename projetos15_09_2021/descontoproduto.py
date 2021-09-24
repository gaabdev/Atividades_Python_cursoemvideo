#Author: Gabriel Silva
#Date: 15/09/2021

#Algoritmo que ler preço do produto e mostre o novo preço com 5% de desconto.

nomeproduto = input('Digite o nome do produto: ')
precoproduto = float(input('Digite o preço do produto: '))

desconto = (precoproduto * 0.05) 
novopreco = precoproduto - desconto

print('>'*35)
print('Produto: {}'.format(nomeproduto))
print('>'*35)
print('De R$ {} por apenas R$ {}'.format(precoproduto, novopreco))
print('>'*35)
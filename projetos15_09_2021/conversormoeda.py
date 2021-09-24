#Author: Gabriel Silva
#Date: 5/09/2021

#Algoritmo que leia o valor em dinheiro que uma pessoa tem na carteira e imprima quantos dólares a mesma pode comprar.
#Dólar Americano = R$ 4.17
#Euro = R$ 6.20
#Libra esterlina = R$ 7.25
#Iene = R$ 20.91
#Dólar Australiano = R$ 3.82
#Franco Suíço = R$ 5.98
#Dólar Canadense = R$ 4.78
#Renminbi (Yuan) = R$ 0.88
#Peso Argentino = R$ 0.05
#Lira Turca = R$ 0.61

print('')
real = float(input('Digite quanto dinheiro você tem na carteira: R$ '))
print('')
dolaramericano = real / 4.17
euro = real / 6.20
libraesterlina = real / 7.25
iene = real / 20.91
dolaraustraliano = real / 3.82
francosuiço = real / 5.98
dolarCanadense = real / 4.78
renminbiyuan = real / 0.88
pesoargentino = real / 0.05
liraturca = real / 0.61


print('Digite o numero da conversão que deseja fazer: ')
conversao = int(input(f'1 - Dólar Americano | 2 - Euro 3 - Libra esterlina | 4 - Iene | 5 - Dólar Australiano | 6 - Franco Suíço | 7 - Dólar Canadense | 8 - Renminbi(Yuan) | 9 - Peso Argentino | 10 - Lira Turca |: '))
print('')
print('Você escolheu a opção {}'.format(conversao))
print('>'*45)
#Conversão Dolar Americano
if conversao == 1:
    print('Com R$ {}, você pode comprar $ {:.2f}.'.format(real, dolaramericano))
    #Conversão Euro
elif conversao == 2:
    print('Com R$ {}, você pode comprar US$ {:.2f}.'.format(real, euro))
    #Conversão Libra esterliana
elif conversao == 3:
    print('Com R$ {}, você pode comprar $ {:.2f}.'.format(real,libraesterlina))
    #Conversão Iene
elif conversao == 4:
    print('Com R$ {}, você pode comprar Y {:.2f}.'.format(real,iene))
    #Conversão Dólar Australiano
elif conversao == 5:
    print('Com R$ {}, você pode comprar $ {:.2f}.'.format(real, dolaraustraliano))
    #Conversão Franco Suíço
elif conversao == 6:
    print('Com R$ {}, você pode comprar F {:.2f}.'.format(real, francosuiço))
    #Conversão Dólar Canadense
elif conversao == 7:
    print('Com R$ {}, você pode comprar $ {:.2f}.'.format(real, dolarCanadense))
    #Conversão Yuan
elif conversao == 8:
    print('Com R$ {}, você pode comprar Y {:.2f}.'.format(real, renminbiyuan))
    #Conversão Peso Argentino
elif conversao == 9:
    print('Com R$ {}, você pode comprar $ {:.2f}.'.format(real, pesoargentino))
    #Conversão Lira Turca
elif conversao == 10:
    print('Com R$ {}, você pode comprar $ {:.2f}.'.format(real, liraturca))     
print('>'*45)                        



       


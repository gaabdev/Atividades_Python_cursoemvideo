#Author: Gabriel Silva
#Date: 15/09/2021

#Algoritmo que leia o salário de um funcionario e mostre o novo salario com 15% de aumento.

salariofuncionario = float(input('Digite o seu salário: '))
aumento = salariofuncionario * 0.15
novosalario = salariofuncionario + aumento

print('')
print('#Seu salário atual é de R$ {}'.format(salariofuncionario))
print('#Você teve um aumento de 15% no seu salário.')
print('*'*30)
print('SALÁRIO ATUAL: R$ {}'.format(novosalario))
print('*'*30)
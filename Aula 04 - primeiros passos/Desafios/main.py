#Author: Gabriel Silva
# Date: 13/09/2021


#Desafio 01 - Script python que ler o nome de uma pessoa e imprime uma mensagem de boas vindas de acordo com o nome digitado.


nome = str(input('Digite o seu nome: '))
print(f'Olá {nome}, seja bem vindo(a)!')


#Desafio 02 - Script python que ler o dia, mês e ano de uma pessoa e mostre  uma mensagem com a data formatada.


entradadia = int(input('Digite o dia do seu nascimento: '))

'''Decidi não adicionar um tipo de variável para o 
identificador, pois o usuário pode escrever tanto 
como int quanto como strig, seu mês de nascimento.'''
entradames = (input('Digite o meŝ do seu nascimento: ')) 

entradaano = int(input('Digite seu ano de nascimento: '))
print(f'Você nasceu no dia {entradadia}, do mês {entradames}, no ano {entradaano}.')

verificaresp = str(input('Se seus dados estão corretos, digite "sim", caso contrário, digite "não: '))
correto = 'sim' and 'Sim' and 'SIM'
if verificaresp == correto:
    print('Dados corretos!')
else:
    print("Repita o procedimento novamente!")


#Desafio 03 - Script que ler dois números e imprime a soma entre eles.


numero1 = input('Digite um número: ')
numero2 = input('digite outro número: ')
soma = numero1 + numero2

print(f'A soma entre {numero1} e {numero2}, é {soma}.')
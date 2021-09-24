#Author: Gabriel Silva
#Create: 14/09/2021

#Desafios
#01 - Programa que leia algo e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre.

leitordados = input('Digite algo na tela: ')


print(type(leitordados))
print(f'Pertence ao alfabeto? {leitordados.isalpha()}')
print(leitordados.isalnum()) #Possui letras e números
print(leitordados.isascii()) #possui caracteres ASCII
print(leitordados.isdecimal()) #É um número decimal
print(leitordados.isdigit()) #Possui um digito
print(leitordados.isidentifier()) #É um identificador
print(leitordados.islower()) # Letras minusculas
print(leitordados.isupper()) #Letras maiusculas
print(leitordados.isnumeric()) #Possui apenas numeros
print(leitordados.isspace()) #Possui apenas espaçamento
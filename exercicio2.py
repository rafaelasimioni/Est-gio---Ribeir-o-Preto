'''2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;'''

lista = []
palavra = str(input('Digite uma palavra: ')).upper()
lista.append(palavra)
print(lista)

cont=0
for letra in palavra:
    if letra == 'A':
        cont+=1


if letra == 'A' in palavra:             
    print(f'\nExiste a letra "a" na sua palavra e ela está presente {cont} vezes\n')

else:
    print('\nNÃO existe a letra "a" na sua palavra\n')



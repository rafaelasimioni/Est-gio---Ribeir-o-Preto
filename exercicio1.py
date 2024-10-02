'''1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''
fibo = [] #armazenei os número de Finonacci em uma lista 
numero = 0

def conferir(): #função para conferir se o número digitado faz parte da sequência
    if numero in (fibo):
        print()
        print('\n Seu número faz parte da sequência de Fibonacci\n')
    else:
        print()
        print('\n Seu número NÃO faz parte da sequência de Fibonacci\n')


def fibonacci(): #função para calcular a sequência de Fibonacci
    n = 50 #vai calcular até 50 números
    F1 = 0
    F2 = 1

    fibo.append(F1)
    fibo.append(F2)

    print('{} -> {}'.format(F1,F2), end=' ')
    cont=3
    while cont<= n:
        F3 = F1 + F2
        fibo.append(F3)
      
        print(' -> {}'.format(F3), end=' ')
        F1 = F2
        F2 = F3
        cont+=1 

numero = int(input('Digite um número: '))

fibonacci()
conferir()
